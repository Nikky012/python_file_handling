lines_seen = set()  
outfile = open('d1.txt', "w")
infile = open('m1.txt', "r")
print("The file m1.txt is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:  
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("The file d1.txt is as follows")
for line in open('d1.txt', "r"):
    print(line)

with open(r"C:\pythonprograms\d1.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)


# 580465
