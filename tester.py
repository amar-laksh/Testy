import re
Jkb = {
        'import':r'[\t ]*?import[\t ]*?([a-zA-Z0-9\*\.]*);',
        'varPriv':r'',
        'varPub':r'',
        'varPro':r'',
        'varFinal':r'',
        'var'
    }
Pykb = {
        'def':r'.*?def.*?\( *self *\) *?:$|.*?def.*?\( *\) *?:$',
        'defParam':r'.*?def.*?\(self\).?:.*?'
      }
f = open('../java-IDE/CodingWindow.java','r')

for i in f.readlines():
    if re.match(Jkb['import'],i):
        print re.findall(Jkb['import'],str(i))
    
    if re.match(Jkb[''])
