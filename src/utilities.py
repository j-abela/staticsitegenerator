import re
from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode("img", "", props)
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if old_nodes == []:
        return []
    
    for old_node in old_nodes:
        # Only process TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Split node on delimiter
        segments = old_node.text.split(delimiter)

        # Check for invalid markdown syntax
        if len(segments) % 2 == 0:
            raise Exception(f"invalid markdown syntax - unmatched delimiter '{delimiter}'")
                    
        for i in range(len(segments)):
            # Even indices are TEXT, odd indices are special text type
            current_text_type = TextType.TEXT if i % 2 == 0 else text_type
            new_nodes.append(TextNode(segments[i], current_text_type))
            
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 