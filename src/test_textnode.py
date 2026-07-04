import unittest
from textnode import *
from funcs import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a different text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_TextType(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_emptyString(self):
        node = TextNode("", TextType.PLAIN_TEXT)
        node2 = TextNode('', TextType.PLAIN_TEXT)
        self.assertEqual(node, node2)

    def test_plain_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_text(self):
        node = TextNode("This is an italic text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_text(self):
        node = TextNode(
            "This is a link text node", TextType.LINK, "https://www.boot.dev"
            )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"}) 

    def test_image_text(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "http://www.randomimageurl.com/blah.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {
                "src": "http://www.randomimageurl.com/blah.jpg", 
                "alt": "This is an image text node"
                }
            )

    def test_split_bold(self):
        node1 = TextNode("This is a text node with **bold text** in it.", TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_delimiter([node1], "**", TextType.BOLD_TEXT), 
                    [
                        TextNode("This is a text node with ", TextType.PLAIN_TEXT),
                        TextNode("bold text", TextType.BOLD_TEXT),
                        TextNode(" in it.", TextType.PLAIN_TEXT)
                    ]
                    )

    def test_split_italics(self):
        node1 = TextNode("This is a text node with _italic text_ in it.", TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_delimiter([node1], "_", TextType.ITALIC_TEXT),
                         [
                            TextNode("This is a text node with ", TextType.PLAIN_TEXT),
                            TextNode("italic text", TextType.ITALIC_TEXT),
                            TextNode(" in it.", TextType.PLAIN_TEXT)
                         ]
                         )

    def test_split_code(self):
        node1 = TextNode("This is a text node with `code text` in it.", TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_delimiter([node1], "`", TextType.CODE_TEXT),
                        [
                            TextNode("This is a text node with ", TextType.PLAIN_TEXT),
                            TextNode("code text", TextType.CODE_TEXT),
                            TextNode(" in it.", TextType.PLAIN_TEXT)
                        ]
                        )

    def test_split_start_with_delimiter(self):
        node1 = TextNode(
            "_This_ is a text node with italic text in it.", TextType.PLAIN_TEXT
                        )
        self.assertEqual(split_nodes_delimiter(
            [node1], "_",
            TextType.ITALIC_TEXT
            ),
            [
                TextNode("This", TextType.ITALIC_TEXT),TextNode(
                    " is a text node with italic text in it.",
                    TextType.PLAIN_TEXT
                    )
            ]
            )

    def test_split_end_with_delimiter(self):
        node1 = TextNode(
            "This is a text node with bold text in **it.**", TextType.PLAIN_TEXT
            )
        self.assertEqual(split_nodes_delimiter([node1], "**", TextType.BOLD_TEXT),
                        [
                            TextNode(
                                "This is a text node with bold text in ",
                                TextType.PLAIN_TEXT
                                ),
                            TextNode("it.", TextType.BOLD_TEXT)
                        ]
            )
        
    def test_split_no_delimiters(self):
        node1 = TextNode("This is a text node with italic text in it.", TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_delimiter([node1], "_", TextType.ITALIC_TEXT),
                        [
                            TextNode("This is a text node with italic text in it.", TextType.PLAIN_TEXT)
                        ]
                        )

    def test_split_multiple_plaintext_nodes(self):
        pass

    def test_split_mixed_nodes(self):
        pass

    def test_split_multiple_node_type(self):
        pass


if __name__ == "__main__":
    unittest.main()