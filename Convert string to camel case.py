def to_camel_case(text):
    #your code here
    if '-' in text:
        texta = text.replace('_', '-')
        a = str.split(texta, '-')
        for i in range(1, len(a)):
            a[i] = a[i].capitalize()
        return ''.join(a)
    elif '_' in text:
        textb = text.replace('-', '_')
        b = str.split(textb, '_')
        for i in range(1, len(b)):
            b[i] = b[i].capitalize()
        return ''.join(b)
    else:
        return text


"""
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
"""


"""
The if s else s part takes car of handling empty strings:

if the input string is not null (if s meaning when s is True, 
because it exists), then the first part will be executed: return the camelcase string;
otherwise when an empty string is received (s is False, because it's null): 
then just return the empty string (else s) as required in the test cases
"""
