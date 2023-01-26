with open('file_new.txt', 'w+') as f:   # create a new file or truncates it
    f.write("test 1\n")
    f.write("test 2\n")
    f.write("test 3\n")             # now the file pointer is at the end
    f.seek(0)                       # move the file pointer to the beginning
    lines = f.read()                # read it, now we can read!
    print(lines)                    # print it
