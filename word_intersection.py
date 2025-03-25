def word_intersection():
    st1=input('enter first word:')
    st2=input('enter first word:')

    inters=set(st1.lower())&set(st2.lower())
    print('common letters:',inters)

word_intersection()
