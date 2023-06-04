def frombinary(code):
    print(True)
    while (len(code)%8)!=0:
        code="0"+code
    list=[]
    temp=""
    i2=0
    for i in code:
        if (i2<8):
            temp=temp+i
            i2+=1
        else:
            list.append(temp)
            temp=i
            i2=1
    list.append(temp)
    result=""
    for i in list:
        result=result+(chr(int(i,2)))
    return result

def tobinary(text):
    return (''.join(format(ord(i), '08b') for i in text)).replace(" ","")[1:]