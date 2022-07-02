new_list=[]

def flatten(l):

    for element in l:
        if isinstance(element,list):
            flatten(element)
        else:
            new_list.append(element)
    return new_list

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))