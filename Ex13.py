#Program by:Kashish Gupta
#Roll No. 32
#List Assignment No.
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
age=[15,25,39,40,10,5,75,45,52,14]
minor=[]
major=[]
for i in age:
    if(i<18):
        minor.append(i)
        print("minor")
    else:
        major.append(i) 
        print("major")


