import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_repr_only_tag(self):
        node = HTMLNode("a")
        self.assertEqual('HTMLNode(a, None, None, None)', node.__repr__())

    def test_repr(self):
        node = HTMLNode(
            "a",
            "Click here",
            HTMLNode("p", "Lorem ipsum"),
            {
                "href": "http://google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(
            "HTMLNode(a, Click here, HTMLNode(p, Lorem ipsum, None, None), {'href': 'http://google.com', 'target': '_blank'})", 
            node.__repr__())
    
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            props = {
                "href": "http://google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(' href="http://google.com" target="_blank"', node.props_to_html())

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    #Leaf Tests
    def test_values(self):
        node = LeafNode(
            "div",
            "I wish I could read",
            {"target": "_blank"}
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            {'target': '_blank'}
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_a_(self):
        node = LeafNode(
            "a",
            "Click here",
            props = {
                "href": "http://google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(
            node.to_html(), 
            '<a href="http://google.com" target="_blank">Click here</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Lorem ipsum")
        self.assertEqual(node.to_html(), "Lorem ipsum")

    #ParentNode Tests
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
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
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()