#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
def palind(r):
    e = len(r) - 1
    s = 0
    while (s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True


r = (1,2,3,3,2,1)

if(palind(r)):
    print("The tuple is a flip-flop")
else:
    print("The tuple is not a flip-flop")


