from enum import Enum
from htmlnode import ParentNode
from utilities import text_to_textnodes, text_node_to_html_node
from textnode import  TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered"
    OLIST = "ordered"

def markdown_to_blocks(markdown):
    old_blocks = markdown.split("\n\n")
    new_blocks = []
    for old_block in old_blocks:
        if old_block == "":
            continue
        new_blocks.append(old_block.strip())
    return new_blocks

def block_to_block_type(block):
    if block == "":
        return BlockType.PARAGRAPH
    if is_heading(block):
        return BlockType.HEADING
    
    # Cases where individual lines need to meet certain conditions
    lines = block.split('\n')

    # For code
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    # For quotes
    if all_lines_match(lines, lambda _: ">"):
        return BlockType.QUOTE

    # For unordered lists
    if all_lines_match(lines, lambda _: "- "):
        return BlockType.ULIST

    # For ordered lists
    if all_lines_match(lines, lambda i: f"{i+1}. "):
        return BlockType.OLIST
        
    return BlockType.PARAGRAPH

def is_heading(text):
    # Split the text by spaces
    parts = text.split(' ', 1)
    
    # Check if the first part consists only of # characters
    if len(parts) > 1 and parts[0].startswith('#') and all(char == '#' for char in parts[0]):
        # Check if the number of # is between 1 and 6
        num_hashes = len(parts[0])
        return 1 <= num_hashes <= 6
    
    return False

def all_lines_match(lines, prefix_func):
    for i in range(len(lines)):
        expected_prefix = prefix_func(i)
        if not lines[i].startswith(expected_prefix):
            return False
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match(block_type):
        case (BlockType.PARAGRAPH):
            return paragraph_to_html_node(block)
        case (BlockType.HEADING):
            return heading_to_html_node(block)
        case (BlockType.CODE):
            return code_to_html_node(block)
        case (BlockType.OLIST):
            return olist_to_html_node(block)
        case (BlockType.ULIST):
            return ulist_to_html_node(block)
        case (BlockType.QUOTE):
            return quote_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    counter = 0
    for char in block:
        if char == "#":
            counter += 1
        else:
            break
    if counter + 1 >= len(block):
        raise ValueError(f"invalid heading level: {counter}")
    else:
        text = block[counter + 1:]
        children = text_to_children(text)
        return ParentNode(f"h{counter}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    else:
        text = block[4:-3]
        raw_text_node = TextNode(text, TextType.TEXT)
        child = text_node_to_html_node(raw_text_node)
        code = ParentNode("code", [child])
        return ParentNode("pre", [code])

def olist_to_html_node(block):
    pass

def ulist_to_html_node(block):
    pass

def quote_to_html_node(block):
    pass
