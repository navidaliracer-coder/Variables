#python program to illistrate the use of 'is' identity operater
# of 'is' indentity opeater
x = 5
if (type(x) is int ):
    print("True!")
else:
    print("false")



x = 5.0
if (type(x) is not float):
    print("True!")
else:
    print("false")


x = 20
y = 20
if (x is y):
    print ("X & Y are the SAME IDENTITY!!!!")
else:
    print("X & Y are not the SAME IDENTITY!!!!")
