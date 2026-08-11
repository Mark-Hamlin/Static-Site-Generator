
def markdown_to_blocks(markdown):
    new_markdown_list = []
    split_markdown = markdown.split("\n\n")
    for mark in split_markdown:
        if len(mark) != 0:
            new_markdown_list.append(mark.strip())
    return new_markdown_list
