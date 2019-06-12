fo = open("result_16.xyz", "r")
w = open("16.xyz","w")
for line in fo.readlines():
    if (line[0]!="#"):
           w.write(line)
    else:
           w.write("100.00000   100.00000   100.00000\n")
fo.close()
