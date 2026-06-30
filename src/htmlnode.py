class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None,
                 children: list | None = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html function has not been implemented")
    
    def props_to_html(self):
        if self.props is None:
            return None
        else:
            html_props = ""
            for k, v in self.props.items():
                html_props += f'{k}="{v}" '
            return html_props.strip()
        
    def __repr__(self):
        return f"HTMLNode -> {{tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}}}"