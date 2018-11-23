import re

data = """
kim, fail, fail
shin, pass, fail
"""

n = re.compile("(\w+[,]\w+[,])\w+")
print(n.sub("\g<1>pass", data))

n2 = re.compile("fail$",re.MULTILINE)
print(n2.sub('pass',data))
