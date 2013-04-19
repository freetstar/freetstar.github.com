import os

filelists =  os.listdir(os.getcwd())


def delMoreTag(f):
    newlines = []
    with open(f,'r')  as content:
        for line in content.readlines():
            newlines.append(line.replace('',''))
    with open(f,'w') as content:
        for line in newlines:
            content.write(line)

def delMultiblankline(f):
    file = open(f,'r+')
    lines = file.readlines()
    new_lines = list(set(lines))
    print new_lines
    # for line in new_lines:
    #     file.write(line) 
    # file.close();

def process(f):
    delMoreTag(f)
    delMultiblankline(f)


[process(f) for f in filelists]
    
