    # initialize with all hours for day = 00000 invalidated
    s = "0-31"
    a = 0
    # for days 00001 to 11111
    for day in range(1,32):
        a += 1 << 5     # increment day
        s += ", " + str(a+24) + "-" + str(a+31) # add invalid hours for that day
    print(s)