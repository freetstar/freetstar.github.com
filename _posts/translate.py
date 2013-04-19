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
    for lines in fileinput.FileInput(f, inplace=1): 	
        lines = lines.strip()
        if lines == '': continue

def process(f):
    delMoreTag(f)
    delMultiblankline(f)


[process(f) for f in filelists]
    
