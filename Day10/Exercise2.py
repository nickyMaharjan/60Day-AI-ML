from sklearn.model_selection import train_test_split

# Example list of 10 students
students = ['Anna', 'Ben', 'Cara', 'Dan', 'Eva', 'Finn', 'Gina', 'Henry', 'Ivy', 'Jack']

# Split without random_state
train1, test1 = train_test_split(students, test_size=0.2)
train2, test2 = train_test_split(students, test_size=0.2)

# Split with random_state
train3, test3 = train_test_split(students, test_size=0.2, random_state=42)
train4, test4 = train_test_split(students, test_size=0.2, random_state=42)

# Show results
print("No random_state (first split):")
print("Train:", train1)
print("Test:", test1)

print("\nNo random_state (second split):")
print("Train:", train2)
print("Test:", test2)

print("\nWith random_state=42 (first split):")
print("Train:", train3)
print("Test:", test3)

print("\nWith random_state=42 (second split):")
print("Train:", train4)
print("Test:", test4)
