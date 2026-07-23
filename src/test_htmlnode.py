import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, None)
        node2 = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertNotEqual(repr(node), repr(node2))
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("div", "This is a div", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")
    def test_leaf_to_html_span_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
