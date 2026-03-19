#Program by:Kashish Gupta
#Roll No. 32
#List Assignment No.
#Given a list of 10 student marks, count how many students scored above 40.
Student_marks=[35,42,28,50,86,56,37,10,40,90]
count=0
for i in Student_marks:
    if i>40:
        count+=1
        print(count)