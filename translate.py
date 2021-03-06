import os

filelists =  os.listdir(os.getcwd())

def delMoreTag(f):
    newlines = []
    with open(f,'r')  as content:
        for line in content.readlines():
            newlines.append(line.replace('<!-- more -->',''))
    with open(f,'w') as content:
        for line in newlines:
            content.write(line)

def delSlug(f):
    newlines = []
    with open(f,'r')  as content:
        for line in content.readlines():
            newlines.append(line.replace('slug',''))
    with open(f,'w') as content:
        for line in newlines:
            content.write(line)

def delMultiblankline(f):
    file = open(f,'r+')

    lines = file.readlines()

    index_list = []
    for index, line in enumerate(lines):
        if not line.strip():
            index_list.append(index)

    index_to_del = []
    for i in range(len(index_list)):
        try:
            if index_list[i] + 1 == index_list[i + 1]:
                index_to_del.append(index_list[i])
        except IndexError:
            pass

    for j,i in enumerate(index_to_del):
        del lines[i-j]

    file.seek(0)
    file.truncate()
    file.write(''.join(lines))
    file.close()

def process(f):
#    delMoreTag(f)
#    delMultiblankline(f)
     delSlug(f)

[process(f) for f in filelists]

