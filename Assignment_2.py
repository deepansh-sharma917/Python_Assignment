#r+
with open('file.txt', 'r+') as f:
    print(f.read())
    f.write("new line \n")
    
# w+    
with open('file.txt', 'w+') as f:   
    f.write("test 1\n")
    f.write("test 2\n")
    f.write("test 3\n")             
    f.seek(0)                       
    lines = f.read()                
    print(lines)                    
with open('file.txt', 'a+') as f:
    f.seek(0)                       
    lines = f.readlines()           
    f.write("\n" + str(len(lines))) 

with open('file.txt','r') as f:
    print(f.read())
