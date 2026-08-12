from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
def is_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True
def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
       if not line.startswith("- "):
          return False
    return True
def is_ordered_list(block):
    lines = block.split("\n")
    i = 1
    for line in lines:
        expectected_prefix = f"{i}. "
        if not line.startswith(expectected_prefix):
            return False
        i+=1
    return True

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH



def markdown_to_blocks(markdown):
    new_markdown_list = []
    split_markdown = markdown.split("\n\n")
    for mark in split_markdown:
        if len(mark) != 0:
            new_markdown_list.append(mark.strip())
    return new_markdown_list
