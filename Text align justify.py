def justify(text, width):
    # your code here
    a = len(text)/width
    width -= 1
    for i in range(a):
        if text[width] == ' ':
            text = text[:width-1] + '\n' + text[width-1:]
            width += width
        else:
            text = text[:width] + '\n' + text[width:]
    return text



"""
def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)
"""
