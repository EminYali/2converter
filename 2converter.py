def int(input):
    try:
        switcher = {"0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,}
        leng=len(input)
        zero=1
        out_number=0
        for i in range(leng):
            b = switcher.get(input[i])
            for j in range(leng-i-1):
                zero*=10
            b*=zero
            zero=1
            out_number+=b
        return out_number
    except:
        pass
def str(input):
    switcher = {0: "0",1: "1",2: "2",3: "3",4: "4",5: "5",6: "6",7: "7",8: "8",9: "9",}
    motkat=10
    list=[]
    output=""
    outputconver=""
    for i in range(input):
        y=input
        y=y%motkat
        input-=y
        motkat*=10
        if y==0:
            break
        else:
            list.append(y)
    for j in list:
        while True:
            if(j==1 or j==2 or j==3 or j==4 or j==5 or j==6 or j==7 or j==8 or j==9):
                output += switcher.get(j)
                break
            else:
                j/=10
    long=len(output)-1
    while True:
        outputconver+=output[long]
        if(long==0): break
        long-=1
    return outputconver