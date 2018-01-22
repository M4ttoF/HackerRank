import sys

def timeConversion(s):
    # Complete this function
    end=s[-2:]
    s=s[:-2]
    sTime=s.split(':')
    iTime=[int(sTime[0]),int(sTime[1]),int(sTime[2])]
    if end.upper()=="PM":
        iTime[0]+=12
        if(iTime[0]==24):
            iTime[0]=12;
    if end.upper()=="AM" and iTime[0]==12:
        iTime[0]=0
    sTime=[str(iTime[0]),str(iTime[1]),str(iTime[2])]
    for i in range(0,3):
        if len(sTime[i])==1:
            sTime[i]='0'+sTime[i]
    s=sTime[0]+':'+sTime[1]+':'+sTime[2]
    return s
        
s = input().strip()
result = timeConversion(s)
print(result)