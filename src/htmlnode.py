
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("Not implemented yet")

    def props_to_html(self):
        if not self.props:
            return ""
        prop_str = ""
        for prop in self.props:
            prop_str += f' {prop}="{self.props[prop]}"'
        return prop_str

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return self.value
        props_text = self.props_to_html()
        return f"<{self.tag}{props_text}>{self.value}</{self.tag}>"

    
