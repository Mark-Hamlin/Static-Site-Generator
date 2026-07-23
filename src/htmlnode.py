class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        returned_string = ""
        if self.props is None:
            return returned_string
        for key in self.props:
            returned_string += f"{key} = {self.props[key]}"
        return returned_string
    def __repr(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
