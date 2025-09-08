# Make it work for multiple students:

# students = [
#     {"name": "Ashu", "marks": [80, 90, 85]},
#     {"name": "Riya", "marks": [70, 60, 75]}
# ]


# Expected Output:

# Ashu → 85.0
# Riya → 68.3


students = [
    {"name": "Ashu", "marks": [80, 90, 85]},
    {"name": "Riya", "marks": [70, 60, 75]}
]


for student in students:
    toatl = sum(student["marks"])
    avg = toatl / len(student["marks"])
    print(student["name"], "→", round(avg, 1))
