inp=input("Enter You sentence:")

def count_frequency(sentence):
    freq={}
    word=""
    for ch in sentence:
        if (ch==" " or ch=="." or ch=="!"):
            if word!="":
                if word in freq:
                    freq[word.lower()]+=1
                else:
                    freq[word.lower()]=1
                word=""            
        if "a"<=ch.lower()<="z":
            word+=ch
        else:
            continue
        
    return freq

hashmap=(count_frequency(inp))

my_dict=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
for i in range(5):
    print(my_dict[i][0])