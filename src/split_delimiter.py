from htmlnode import *
from textnode import *
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_node_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_node_list.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 ==0:
            raise Exception("Delimiter doesn not match")
        for index,section in enumerate(sections):
            if len(section) == 0:
                continue
            if index %2 == 0:
                new_node_list.append(TextNode(section,TextType.TEXT))
            else:
                new_node_list.append(TextNode(section,text_type))

    return new_node_list
