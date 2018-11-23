import re

data = """
kim, fail, fail
shin, pass, fail
"""

n = re.compile("(\w{3})[,](\w{4})[,](\w{4})")
print(n.sub("\g<1>, \g<3>, pass", data))

n2 = re.compile("fail$",re.MULTILINE)
print(n2.sub('pass',data))
