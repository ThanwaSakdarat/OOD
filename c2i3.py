from re import I


print("*** Mod Position ***")
word,num = input("Enter Input : ").split(',')
sep = list(word)
sep_two = int(num)

def mod_position(arr, s):
    element = []
    i= 1
    for index in sep:
        if i%s==0:
            element.append(sep[i-1])  
        i=i+1
    print(element)

mod_position(sep,sep_two)


