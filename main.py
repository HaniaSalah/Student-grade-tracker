import os

FILE_PATH="grades.txt"

grade=[]
for i in range(5):
    grade.append(int(input("Enter your grade: ")))
print("The average= ",sum(grade)/5)
try:
    file=open(FILE_PATH,"a")
    file.write( str(grade))
    file.write("\n")

except ValueError as e:
    print(f"Invalid grade: {e}")
