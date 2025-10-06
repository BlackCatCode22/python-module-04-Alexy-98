han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wrds = line.split()
    #Guardian Pattern, helps from blow up
    #Can make stronger, made a compound statement
    if len(wrds) < 3 or wrds[0] != "From":
        #Guardian always comes before
        continue
    print(wrds[2])