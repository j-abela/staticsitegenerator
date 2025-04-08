from textnode import TextNode, TextType
from text_to_html_transformer import *

def main():
    text_node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
    html_node = text_node_to_html_node(text_node)
    print(html_node.to_html())
main()