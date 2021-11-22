import ipaddress
a_file = open("domain_duplicate.txt", "r")
list_of_lists = []
for line in a_file:
    if line and " " in line:
        stripped_line = line.strip()
        line_list = stripped_line.split()[1]
        list_of_lists.append(line_list)
a_file.close()
with open("domain_ip.txt", "a") as f:
    for l in list_of_lists:
        try:
            ipaddress.ip_address(l)
            f.write(l+ "\n")
        except:
            pass
