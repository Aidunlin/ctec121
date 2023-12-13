# PS 2 - Nutrition Facts
# Aidan Linerud

# Stores apples with their respective calorie counts
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

user_input = input("Item: ").strip().lower()

# Ignore any invalid inputs
if user_input in fruit_calories:
    # Print calories associated with user input
    print(f"Calories: {fruit_calories[user_input]}")
