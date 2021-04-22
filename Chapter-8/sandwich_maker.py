import pyinputplus as pyip

costs = {
    "WHEAT": 2.50,
    "WHITE": 2.50,
    "SOURDOUGH": 3.50,
    "CHICKEN": 2.00,
    "TURKEY": 2.30,
    "HAM": 1.20,
    "TOFU": 1.80,
    "CHEDDAR": 1.50,
    "SWISS": 2.00,
    "MOZZARELLA": 2.80,
    "EXTRA": 2.50,
}


def print_total(sandwich, qty):
    total = 0
    print("\nYour Sandwich: ", sep="")
    for ingredient in sandwich:
        if ingredient:
            ing_price = costs.get(ingredient.upper(), 0)
            total += ing_price
            print(f"\t{ingredient} ({ing_price:.2f}€)")
    print(
        f"\nThe total for ({qty} sandwich{'es' if qty>1 else ''}) is {total*qty:.2f}€")


while True:
    bread = pyip.inputMenu(
        ["Wheat", "White", "Sourdough"], numbered=True, prompt="Please select what type of bread you want: \n")

    protein = pyip.inputMenu(
        ["Chicken", "Turkey", "Ham", "Tofu"], numbered=True)

    cheese = pyip.inputYesNo(prompt="Do you want cheese? ")

    if cheese == "yes":
        cheese_select = pyip.inputMenu(
            ["Cheddar", "Swiss", "Mozzarella"], numbered=True)
    else:
        cheese_select = None

    extra = pyip.inputYesNo(
        prompt="Do you want Mayo, Mustard, Lettuce or Tomato? ")
    extra = "extra" if extra == "yes" else None

    qty = pyip.inputInt("How many sandwiches you want? ", min=1)

    sandwich = [bread, protein, cheese_select, extra]

    break

print_total(sandwich, qty)
