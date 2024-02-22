def interchange(gayulist):
    

    listlen=len(gayulist)
    temp=gayulist[0]
    gayulist[0]=gayulist[listlen-1]
    gayulist[listlen-1]=temp
    return gayulist

gayulist=[1,2,3,4,5]
print(interchange(gayulist))

