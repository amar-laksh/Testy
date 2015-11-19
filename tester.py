import re
Jkb = {
        'package':r'[\t ]*?package[\t ]*?([a-zA-Z0-9\*\.]*);',
        'import':r'[\t ]*?import[\t ]*?([a-zA-Z0-9\*\.]*);',
        'varPriv':r'',
        'varPub':r'',
        'varPro':r'',
        'varFinal':r''
    }
Pykb = {
        'def':r'.*?def.*?\( *self *\) *?:$|.*?def.*?\( *\) *?:$',
        'defParam':r'.*?def.*?\(self\).?:.*?'
      }

def match(line,data):
    count = 0
    c = 0
    found = []
    for i in line:
        if i == data:
            count = count + 1
            found.append(line.index(i,c))
        c = c + 1
    return count,found

def iterate(this,i):
    c = 0
    try:
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        for k in this:
            print this[i][c]
            c = c + 1
    except:
        pass
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
def scope(fileName):
    startScope = []
    endScope = []
    this = []
    f = open(fileName,'r')
    c = 0
    for i in f.readlines():
        r1,o1 = match(i,"{")
        r2,o2 = match(i,"}")
        if r1 == 1:
            startScope.append(c)
        if r2 == 1:
            endScope.append(c)
            g = open(fileName,'r')
            this.append(g.readlines()[startScope[-1]:endScope[-1]])
        c = c + 1
    for i in range(0,len(this)):
        iterate(this,i)
    
    f.close()
scope('../java-IDE/CodingWindow.java')
"""
for i in f.readlines():
    if re.match(Jkb['import'],i):
        print re.findall(Jkb['import'],str(i))
    if re.match(Jkb['package'],i):
        print re.findall(Jkb['package'],str(i))    
    if "{" in i:
        print c 
    c = c + 1
"""
