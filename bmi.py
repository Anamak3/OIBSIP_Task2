
bmi_categories = {
    "Underweight": (None, 18.5),
    "Normal": (18.5, 25),
    "Overweight": (25, 30),
    "Obese": (30, None)
}
def calculate_bmi(weight, height):

    return weight / (height ** 2)
def get_bmi_category(bmi):
    for category, (lower, upper) in bmi_categories.items():
        if (lower is None or bmi >= lower) and (upper is None or bmi < upper):
            return category
    return "Invalid BMI"
def main():

    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in m): "))
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")
if __name__ == '__main__':
    main()





