import os

file = open("web.html")

line = file.read()
file.close()
line = line.replace(u'$+=', u'\n')
line = line.replace(u'?()', u'<')
line = line.replace(u'?)(', u'>')
print(line)
