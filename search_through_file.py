fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    #Skips uninteresting lines
    if line.startswith("From "):
        continue
    #Process interesting lines
    print(line)

#Finding and searching
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == 1: continue
    print(line)