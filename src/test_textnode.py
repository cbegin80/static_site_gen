import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2, "Failed identical node test")

    def test_different_text(self):
        print("Testing different text")
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a different text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2, "Failed different text test")

    def test_different_TextType(self):
        print("Testing different TextType")
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2, "Failed different TextType test")

    def test_url_none(self):
        print("Testing default URL")
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2, "Failed url=None/default test")

    def test_emptyString(self):
        print("Testing empty string")
        node = TextNode("", TextType.PLAIN_TEXT)
        node2 = TextNode('', TextType.PLAIN_TEXT)
        self.assertEqual(node, node2, "Failed empty string test")

if __name__ == "__main__":
    unittest.main()