def alphabet_position(text):
    import string
    t = (text.translate(None, string.punctuation)).replace(" ", "")
    t = str.lower(t)
    output = ""
    for c in t:
        if ord(c) > 96:
            output = output+str(ord(c)-96)+' '
        else:
            output = output + ""
    output = output.rstrip(" ")
    return output


"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) 
    ###
    判断字符ch是否为英文字母，若为英文字母，返回非0（小写字母为2，大写字母为1)
    ###
"""
