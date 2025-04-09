from enum import Enum

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
    # Cases where the entire block is evaluated 
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if is_heading(block):
        return BlockType.HEADING
    
    # Cases where individual lines need to meet certain conditions
    lines = block.split('\n')
    
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