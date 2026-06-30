import unittest
from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()