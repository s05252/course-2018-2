strInput = "aaabbcccccca"
strOutput = "a3b2c6a1"

curChar = ""
count = 0

for i in strInput:
    if curChar ==  i:
        count = count + 1
    else:
        if count != 0:
            print(curChar + str(count), end = '')
        curChar = i
        count = 0
        count += 1


print(curChar + str(count))
