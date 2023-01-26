with open('file.txt', 'a+') as f:
    f.seek(0)
    lines = f.readlines()
    f.write("\n" + str(len(lines)))

with open('file.txt', 'r') as f:
    print(f.read())
