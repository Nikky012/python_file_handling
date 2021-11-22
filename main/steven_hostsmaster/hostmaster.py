f = open(r"C:\pythonprograms\task5\hosts-master\hosts", "r")
list_of_lists = []
for line in f:
    #line.strip()
    list_of_lists.append(line)
f.close()
with open("hostsmaster.txt", "a") as f:
    for l in list_of_lists:
        f.write(l)
        l.rstrip(' ')
print(list_of_lists)
# read mode
file1 = open('hostsmaster.txt','r')
# in write mode
file2 = open('hostsmaster_1.txt','w')
# reading each line from original
# text file
for line in file1.readlines():
    if not (line.startswith('#')):
       
        file2.write(line)
# close and save the files
file2.close()
file1.close()
