# print th average marks of a student
student = {
    "name": "Ashu",
    "marks": [10, 20, 30]
}

toal = 0
for marsk in student["marks"]:
    toal += marsk

avg = toal / len(student["marks"])
print(f"Average marks of {student['name']} is {avg}")