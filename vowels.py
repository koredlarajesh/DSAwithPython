def vowels_string(a):
    s=["a","e","i","o","u"]
    count=0
    for i in a:
        if i in s:
            count=count+1
    return count
a="rajesh"
print(vowels_string(a))