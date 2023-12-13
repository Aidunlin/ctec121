# Midterm P2 - Teach Somebody
# Aidan Linerud
# Loom video: https://www.loom.com/share/87bec4453c6140e98352d61935f67241

#### LISTS VERSUS DICTIONARIES ####


## Definitions ##

define_list = "Stores an ordered sequence of values"

define_dictionary = "Stores values by mapping them to keys"



## Basic syntax ##

cool_list = []  # Square brackets!

cool_dictionary = {}  # Curly braces!



## Items ##
print()
print("ITEMS")
print()

items_in_list = [1, 2, 3]  # Separated with commas

print(items_in_list[0])  # First item indexed with 0

items_in_dictionary = {  # Also separated with commas
    "apples": 1,
    "bananas": 2,
    "carrots": 3,
}

print(items_in_dictionary["apples"])  # Similar to list indexing, but using keys instead



## Containing each other ##
print()
print("CONTAINING EACH OTHER")
print()

dictionaries_in_list = [
    {"name": "apple", "count": 1},
    {"name": "banana", "count": 2},
    {"name": "carrot", "count": 3},
]

print(dictionaries_in_list[1]["name"], dictionaries_in_list[1]["count"])

lists_in_dictionary = {
    "foods": ["apple", "banana", "carrot"],
    "drinks": ["water", "milk", "juice"],
}

print(lists_in_dictionary["foods"][2])



## Iterating lists ##
print()
print("ITERATING LISTS")
print()

# "Why waste time say many print..."

print(items_in_list[0])
print(items_in_list[1])
print(items_in_list[2])

# "... when one print do trick?" - Kevin, The Office

for item in items_in_list:
    print(item)

# These two loops output the same:

for index in range(len(items_in_list)):
    item = items_in_list[index]
    print(index, item)

for index, item in enumerate(items_in_list):
    print(index, item)



## Iterating dictionaries ##
print()
print("ITERATING DICTIONARIES")
print()

# These two loops output the same:

for key in items_in_dictionary:
    print(key, items_in_dictionary[key])

for key, value in items_in_dictionary.items():
    print(key, value)
