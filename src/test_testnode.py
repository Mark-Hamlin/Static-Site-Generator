import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, TextType.BOLD)
    def test_text_type_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text_type, TextType.ITALIC)
    def test_text_type_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node.text_type, TextType.CODE)
    def test_text_type_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.text_type, TextType.LINK)
    def test_text_type_image(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node.text_type, TextType.IMAGE)
    def test_text_type_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text_type, TextType.TEXT)
    def test_text_type_none(self):
        node = TextNode("This is a text node", None)
        self.assertEqual(node.text_type, None)
    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_test_type_not_eq_URL(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    def test_test_type_url(self):
        node = TextNode("This is text node", TextType.CODE, "www.boot.dev")
        self.assertEqual(node.url, "www.boot.dev")
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")




if __name__ == "__main__":
    unittest.main()
