import sys

srcFileName = sys.argv[1]
objFileName = sys.argv[2]

srcFileHandle = open(srcFileName, 'r')
txt = srcFileHandle.read()
space_content = txt.replace("\t", "_"*4)

f = open(objFileName, 'w')
f.write(space_content)
f.close()