import re
a = "...!@BaT#*..y.abcdefghijklm-."
a=a.lower()
a = re.sub('[^\d\w.\-_]','',a)
a = re.sub('\.+', '.' ,a)
a = re.sub('^\.|\.$', '',a)
if not a:
    a = 'a'
if len(a) >= 16:
    a = a[:15]
    a = re.sub('^\.|\.$', '', a)
if len(a) <= 2:
    a = a+a[-1]*(3-len(a))
print(a)