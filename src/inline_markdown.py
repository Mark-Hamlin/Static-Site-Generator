import re
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


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return (matches)
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return (matches)

def split_nodes_image(oldnodes: list[TextNode]) -> list[TextNode]:
    new_node_list = []
    for node in oldnodes:
        text = node.text
        image_text = extract_markdown_images(text)
        previous_split_text = node.text
        for image_tuple in image_text:
            alt_text,url = image_tuple
            delimiter = f"![{alt_text}]({url})"
            split_text = previous_split_text.split(delimiter,1)
            if len(split_text[0]) != 0:
                new_node_list.append(TextNode(split_text[0],TextType.TEXT))
            new_node_list.append(TextNode(alt_text,TextType.IMAGE,url))
            previous_split_text = split_text[1]
        if len(previous_split_text) != 0:
            new_node_list.append(TextNode(previous_split_text,TextType.TEXT))
    return new_node_list


def split_nodes_link(old_nodes: list[TextNode]) -> list [TextNode]:
    new_node_list = []
    for node in old_nodes:
        text = node.text
        image_text = extract_markdown_links(text)
        previous_split_text = node.text
        for image_tuple in image_text:
            alt_text,url = image_tuple
            delimiter = f"[{alt_text}]({url})"
            split_text = previous_split_text.split(delimiter,1)
            if len(split_text[0]) != 0:
                new_node_list.append(TextNode(split_text[0],TextType.TEXT))
            new_node_list.append(TextNode(alt_text,TextType.LINK,url))
            previous_split_text = split_text[1]
        if len(previous_split_text) != 0:
            new_node_list.append(TextNode(previous_split_text,TextType.TEXT))
    return new_node_list
