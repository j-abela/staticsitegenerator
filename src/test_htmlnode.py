import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("p", [child_node], {"prop": "prop value"})
        self.assertEqual(
            parent_node.to_html(),
            '<p prop="prop value"><a href="https://www.google.com">Click me!</a></p>'
        )
if __name__ == "__main__":
    unittest.main()