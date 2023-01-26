# r+ mode
with open('file.txt', 'r+') as f:
    print(f.read())
    f.write("new line \n")
