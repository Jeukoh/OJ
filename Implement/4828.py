import re

def all(line):

    if re.search('<[^/a-z0-9]',line):
        return False

    line = re.sub("&(amp|lt|gt);", " ", line)
    r = re.compile("(&x([a-fA-F0-9]+);)")
    m=r.finditer(line)
    for i in m:
        hex = line[i.span()[0]:i.span()[1]]
        if len(hex)%2 == 0:
            return False
    line = re.sub("&x[a-fA-F0-9]+;", " ", line)

    context = []
    # check 1
    r = re.compile("</?[a-z0-9]+>")
    m = r.finditer(line)
    for i in m:
        tag = i.group()
        if tag.startswith("</"):
            if context:
                start_tag = context.pop()
            else:
                return False
            if tag.replace("/","") != start_tag:
                return False
        else:
            context.append(tag)

    if context:
        return False
    line = re.sub("<[a-z0-9]+/>"," ",line)
    line = re.sub("</?[a-z0-9]+>", " ", line)
    r = re.compile("(<|>|&)")
    m = r.search(line)
    if m:
        return False
    for i in line:
        if not 32 <= ord(i) <= 127:
            return False

    return True


while True:
    try:
        line = input()
    except EOFError:
        break
    if all(line):
        print('valid')
    else:
        print('invalid')