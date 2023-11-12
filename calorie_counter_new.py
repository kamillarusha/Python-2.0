class MealTooBigError(Exception):
    pass

menu = {
    'Hamburger': {'calories': 600, 'price': 5},
    'Cheese Burger': {'calories': 750, 'price': 6},
    'Veggie Burger': {'calories': 400, 'price': 5},
    'Vegan Burger': {'calories': 350, 'price': 5},
    'Sweet Potatoes': {'calories': 230, 'price': 3},
    'Salad': {'calories': 15, 'price': 4},
    'Iced Tea': {'calories': 70, 'price': 1},
    'Lemonade': {'calories': 90, 'price': 2},
}

def calculate_calories(*ordered_items):
    total_calories = 0
    for item in ordered_items:
        if item in menu:
            total_calories += menu[item]['calories']
            if total_calories > 2000:
                raise MealTooBigError("Meal exceeds 2000 calories.")
        else:
            print(f"Sorry, {item} is not in the menu.")
    return total_calories
