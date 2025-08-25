import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()