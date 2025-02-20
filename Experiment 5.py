#Jenoh Sam J B
#URK24CS1154
#A number is perfect Number or not using a function.
print("URK24CS1154")
inventory = { 
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)


#Jenoh Sam J B
#URK24CS1154
#A number is perfect Number or not using a function.
print("URK24CS1154")
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key],'\n')
total = 0
for key in prices:
    money = prices[key] * stock[key]
    print(key ,":",money)
    total += money
print("\nTotal:",total)


#Jenoh Sam J B
#URK24CS1154
#A number is perfect Number or not using a function.
print("URK24CS1154")
groceries = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def bill(food):
    total = 0
    for item in food:
        if stock.get(item, 0) > 0:
            total += prices[item]
            stock[item] -= 1
    return total
print(bill(groceries))



#Jenoh Sam J B
#URK24CS1154
#A number is perfect Number or not using a function.
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]
for student in students:
    print(student["name"])
    print("homework:", student["homework"])
    print("quizzes:", student["quizzes"])
    print("tests:", student["tests"])
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(get_letter_grade(get_average(lloyd))) 
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))
