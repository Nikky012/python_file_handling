filenames = [r'C:\pythonprograms\task5\Ultimate.Hosts.Blacklist-master\domains\domains0.list',
             r'C:\pythonprograms\task5\Ultimate.Hosts.Blacklist-master\domains\domains1.list',
             r'C:\pythonprograms\task5\Ultimate.Hosts.Blacklist-master\domains\domains2.list']
with open('mergedomain.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
with open(r"C:\pythonprograms\main\mergedomain.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)


#Total Lines 580465
