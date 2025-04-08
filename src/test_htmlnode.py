import unittest
from htmlnode import HTMLNode

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
if __name__ == "__main__":
    unittest.main()