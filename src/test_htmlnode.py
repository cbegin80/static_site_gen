import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode -> {tag: None, value: None, children: None, props: None}")

    def test_tag_only(self):
        node = HTMLNode("h")
        self.assertEqual(repr(node), "HTMLNode -> {tag: h, value: None, children: None, props: None}")

    def test_all_properties(self):
        node = HTMLNode("p", "This is a paragraph. I know, I know, it's a short one, but it is one.", ["boldNode1", "italicNode2"], {'class': 'main', 'color': 'black'})
        self.assertEqual(repr(node), "HTMLNode -> {tag: p, value: This is a paragraph. I know, I know, it's a short one, but it is one., children: ['boldNode1', 'italicNode2'], props: {'class': 'main', 'color': 'black'}}")
        self.assertEqual(node.props_to_html(), 'class="main" color="black"')