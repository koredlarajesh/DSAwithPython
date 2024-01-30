def anagram(a,b):
    if len(a)!=len(b):
        return "it's not a anagram"
    c={}
    d={}
    for i in a:
        if i in c:
            c[i]=c[i]+1
        else:
            c[i]=1
    for j in b:
        if j in d:
            d[j]=d[j]+1
        else:
            d[j]=1
    if c==d:
        return "anagram"
    return "not anagram"

a="ramya"
b="myaaa"
print(anagram(a,b))

