import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_repr_only_tag(self):
        node = HTMLNode("a")
        self.assertEqual('HTMLNode("a", None, None, None)', node.__repr__())

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
            "HTMLNode(\"a\", Click here, HTMLNode(\"p\", Lorem ipsum, None, None), {'href': 'http://google.com', 'target': '_blank'})", 
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

if __name__ == "__main__":
    unittest.main()