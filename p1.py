
def oper(opn,check):
    ans=[]
    for ele in data:
        if ele[opn] == check:
            ans.append(ele[0])
    if(len(ans)==0):
        # allans.append("None")
        print("None")
    else:
        # allans.append(ans)
        ans.sort()
        print(ans)


def printf(inlist):
    ans=[]
    tmp=('Gender',inlist[1])
    ans.append(tmp)
    tmp=('Age',int(inlist[2]))
    ans.append(tmp)
    tmp=('Group',int(inlist[3]))
    ans.append(tmp)
    tmp=('Dep',inlist[4])
    ans.append(tmp)
    # allans.append(ans)
    print(ans)


dic={'Gender':1,'Age':2,'Group':3,'Dep':4}
namedic={}
data=[]
allans=[]
indata=input()
cnt=0
while(indata !='competitorEND'):
    indata=indata.split(",")
    tmp=[None]*5
    # print (indata)
    tmp[0]=(indata[0].split(':')[1])
    namedic[tmp[0]]=cnt
    for i in range(4):
        indata[i+1]=indata[i+1].split(':')
        tmp[dic[indata[i+1][0]]]=indata[i+1][1].upper()
    data.append(tmp)
    indata=input()
    cnt+=1

# print(data)

while True:
    try:

        op=input().split()
        if len(op)==2:
            oper(dic[op[0]],op[1].upper())
        elif op[0] in namedic.keys():
            printf(data[namedic[op[0]]])
        else:
            print("None")
            # allans.append("None")


    except EOFError:
        break

# for ele in allans:
#     print(ele)