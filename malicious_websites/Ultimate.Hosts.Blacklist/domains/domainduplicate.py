lines_seen = set()  
outfile = open('domain_duplicate.txt', "w")
infile = open('mergedomain.txt', "r")
print("The file mergedomain.txt is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:  
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("The file domain_duplicate.txt is as follows")
for line in open('domain_duplicate.txt', "r"):
    print(line)

with open(r"C:\pythonprograms\main\domain_duplicate.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)


# 580465
