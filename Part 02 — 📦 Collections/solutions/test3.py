import json

student = {
    "name": "Simon okopi",
    "class": "SS1",
    "position": "first"
}

student["average"] = 99.9
student["sport"] = "football"
student["fave_food"] = "fried rice"
student["class"] = "SS3"
del student["fave_food"]


# print(student)
print(student["name"])
print(student["class"])
print(student["sport"])
print(student["average"])
print(student["position"])
print(student.keys())



if "position" in student:
    print(f'found it: {student["position"]}')
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
