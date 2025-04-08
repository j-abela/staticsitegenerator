import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        singleprop= {"href": "https://www.google.com"}
        node = HTMLNode(props=singleprop)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
        twoprops = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=twoprops)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_node(self):
        leafnode = LeafNode("p", "This is a paragraph")
        self.assertEqual(f"{leafnode}", "HTMLNode(p, This is a paragraph, None, None)")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()