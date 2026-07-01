class HTMLNode():
    def __init__(self, tag: str | None = None, value = None,
                 children: list | None = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html function has not been implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            html_props = ""
            for k, v in self.props.items():
                html_props += f'{k}="{v}" '
            return html_props.strip()
        
    def __repr__(self):
        return f"HTMLNode -> {{tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}}}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value, 
                 props: dict | None = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        html_string = f"<{self.tag}"
        if self.props_to_html() != '':
            html_string += f" {self.props_to_html()}"
        html_string += f">{self.value}</{self.tag}>"
        return html_string
    
    def __repr__(self):
        return f"HTMLNode -> LeafNode -> {{tag: {self.tag}, value: {self.value}, props: {self.props}}}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == "" or self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children == [] or self.children is None:
            raise ValueError("All parent nodes must have children.")
        else:
            html_string = f"<{self.tag}"
            if self.props_to_html() != '':
                html_string += f" {self.props_to_html()}"
            html_string += ">"
            for child_node in self.children:
                html_string += child_node.to_html()
            html_string += f"</{self.tag}>"
        return html_string