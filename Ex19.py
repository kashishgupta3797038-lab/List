#Program by:Kashish Gupta
#Roll No. 32
#List Assignment No.
Attendence=[1,1,1,0,0,1,0,1,0,0,1]
Pcount=0
Acount=0
for i in Attendence:
    if i==1:
        Pcount+=1
    else:
        Acount+=1  
print("Present=",Pcount)         
print("Absent=",Acount)         
Percentage=Pcount/len(Attendence)*100
print(Percentage)
