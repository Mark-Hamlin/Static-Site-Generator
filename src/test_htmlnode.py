import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", None, None)
        node2 = HTMLNode("div", "This is a div", None, {"class": "container"})
        self.assertNotEqual(repr(node), repr(node2))
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("div", "This is a div", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
