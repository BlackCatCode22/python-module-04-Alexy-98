fh = open("mbox-short.txt")
#Puts in whole text

for lx in fh:
    ly = lx.rstrip()
    #Makes a strip, throws away the non-printing characters
    print(ly.upper())
    #Makes it all upper case