from textnode import * 

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    if old_nodes == []:
        return []
    else:
        for node in old_nodes:
            if node.text_type != TextType.PLAIN_TEXT:
                new_nodes.append(node)
            elif delimiter not in node.text:
                new_nodes.append(node)
            else:
                parts = node.text.split(delimiter)
                if len(parts) < 2 or len(parts) % 2 == 0:
                    raise ValueError(
                        "Valid markdown code requires matching delimiters"
                        ) # If there are matching starting/ending tags, number
                        # of parts will always be odd
                for i in range(len(parts)):
                    if parts[i] == '':
                        continue
                    if i % 2 == 0:
                        new_nodes.append(TextNode(parts[i], TextType.PLAIN_TEXT))
                    else:
                        new_nodes.append(TextNode(parts[i], text_type))                       
                
    return new_nodes 