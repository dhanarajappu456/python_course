t = input ("Give me a number\n")
s = str(abs(int(t))) #allow negatives
j = int(s) % int(s[0] + s[-1])
if len(s) > 2: #exclude 2 digits or shorter
    print ((t + " is a gapful number") if j == 0 else (t  + " is not a gapful number"))
else:
    print ("number should be 3 digits or longer\n")