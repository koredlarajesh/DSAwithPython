def left_non_repeating_char(a):
    c={}
    for i in a:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    print("c",c)
    print(c.items())
    for i,j in c.items():
        if j==1:
            return i
    return "only repeated characters are there"

a="geeksforgeeks"
print(left_non_repeating_char(a))