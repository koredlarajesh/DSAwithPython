def reverse_words_string(a):
    c=" "
    for i in a:
        c=  " ".join(i) + c
    print(c)
    words=[]
    current_word=""
    for i in c:
       # current_word=" "
        if i==" ":
            words.append(current_word)
            current_word=""
        else:
            current_word=i+current_word
    words.append(current_word)
    final_sentence=" "
    for i in words:
        final_sentence=final_sentence+" " + i

    return final_sentence
a="i am rajesh koredla sai"
print(reverse_words_string(a))