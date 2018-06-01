def toStringList(node):
    nodelist = [node.toString()]
    if not node.children:
        return nodelist

    for child in node.children:
        entry = toStringList(child)
        if isinstance(entry, list):
            nodelist += entry
        else:
            nodelist.append(entry)

    return nodelist

def childsToStringList(node):
    nodelist = []
    if not node.children:
        return nodelist

    for child in node.children:
        entry = toStringList(child)
        if isinstance(entry, list):
            nodelist += entry
        else:
            nodelist.append(entry)

    return nodelist

def objListToStringList(objects):
    output = []
    for entry in objects:
        output.append(entry.toStringTree())
    return output
