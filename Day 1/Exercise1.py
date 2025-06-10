
fruits = ["apple", "banana", "mango"]
print("List:", fruits)
fruits[1] = "orange"
fruits.append("grape")
print("Updated List:", fruits)

colors = ("red", "green", "blue")
print("Tuple:", colors)
# colors[1] = "yellow" , cannot update a tuple

student = {
    "name": "Suman",
    "age": 21,
    "course": "BCA"
}
print("Dictionary:", student)
student["age"] = 22         
student["grade"] = "A"
print("Updated Dictionary:", student)
