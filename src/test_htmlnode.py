import unittest
from htmlnode import *

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Here's a div!")
        self.assertEqual(node.to_html(), "<div>Here's a div!</div>")

    def test_leaf_to_html_p_with_color(self):
        node = LeafNode("h1", "Red heading", {'color': 'red'})
        self.assertEqual(node.to_html(), '<h1 color="red">Red heading</h1>')