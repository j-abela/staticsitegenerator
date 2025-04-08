from textnode import TextNode, TextType

def main():
    dummynode = TextNode("Some text", TextType.BOLD_TEXT, "https://www.jacob.com.au")
    print(dummynode)
main()