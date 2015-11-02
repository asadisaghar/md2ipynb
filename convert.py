def md2list(line, blockstat, block, blocktype):
    indent = "    "
    indentline = line.startswith(indent)
    emptyline = not line.strip()
    if blockstat == "code":
        if emptyline:
            blockstat = "code"
            block.append(line)
            blocktype.append("code")
        elif indentline:
            blockstat = "code"
            block.append(line)
            blocktype.append("code")
        else:
            blockstat = "md"
            block.append(line)
            blocktype.append("md")
    elif blockstat == "md":
        if emptyline:
            blockstat = "code"
            block.append(line)
            blocktype.append("md")
        elif indentline:
            blockstat = "md"
            block.append(line)
            blocktype.append("md")
        else:
            blockstat="md"
            blocktype.append("md")
            block.append(line)

    return blockstat, block, blocktype

filename = "Day2.md"
with open(filename) as f:
    blockstat = "md"
    block = []
    blocktype = []
    for line in f:
        line = line[:-1]
        blockstat, block, blocktype = md2list(line, blockstat, block, blocktype)
