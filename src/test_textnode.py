import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)    

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.jacob.com.au")         
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.jacob.com.au")
        self.assertEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.jacob.com.au")         
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.jacob.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()