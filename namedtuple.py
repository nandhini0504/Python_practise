from collections import namedtuple
n=int(input())
Students= namedtuple("students",input().split()) # get input of fields from user #Students name of tuple # syntax type name ,field name
# student=students(MARKS,CLASS,NAME,ID)
total=0

for i in range(n):
    total += int(Students(*input().split()).MARKS)
average=total/n
print(average)
print(f'{total / n:.2f}')