import re
kb = {
        'def':r'.*?def.*?\( *self *\) *?:$|.*?def.*?\( *\) *?:$',
        'defParam':r'.*?def.*?\(self\).?:.*?'
      }
f = open('focusTV.py','r')
for i in f.readlines():
    if re.match(kb['def'],i):
        print i
