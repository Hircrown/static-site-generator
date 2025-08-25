import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("Google.com", TextType.LINK, "http://google.com")
        node2 = TextNode("Google.com", TextType.LINK, "http://google.com")
        self.assertEqual(node, node2)

    def test_no_eq_url(self):
        node = TextNode("Google.com", TextType.LINK, "http://google.com")
        node2 = TextNode("Google.com", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_no_eq_text_type(self):
        node = TextNode("Bold", TextType.BOLD)
        node2 = TextNode("Bold", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    # text_node_to_html_node() tests
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text")
    
    def test_code(self):
        node = TextNode("This is a code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code block")

    def test_a(self):
        node = TextNode("Click here", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://google.com">Click here</a>')
    
    def test_img(self):
        node = TextNode("Leclerc wins Monza GP", TextType.IMAGE, "https://charlesleclerc.com/wp-content/uploads/2025/02/Leclerc-Ferrari-Gallery-05-2-Monza.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://charlesleclerc.com/wp-content/uploads/2025/02/Leclerc-Ferrari-Gallery-05-2-Monza.jpg" alt="Leclerc wins Monza GP"></img>'
        )


if __name__ == "__main__":
    unittest.main()