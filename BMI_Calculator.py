import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Overweight"  # Classify all higher BMIs as overweight

def main():
    bmi_records = {"Underweight": 0, "Normal weight": 0, "Overweight": 0}
    while True:
        try:
            weight_input = input("Enter your weight in kilograms (or type 'exit' to finish): ")
            if weight_input.lower() == 'exit':
                break
            weight = float(weight_input)
            height = float(input("Enter your height in meters: "))
            
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            bmi_records[category] += 1
            
            print(f"Your BMI is {bmi:.2f}. You are classified as: {category}.")
            
            continue_prompt = input("Would you like to calculate another BMI? (yes/no): ")
            if continue_prompt.lower() != "yes":
                break
                
        except ValueError:
            print("Please enter valid numbers for weight and height, or type 'exit' to finish.")
        
    
    categories = list(bmi_records.keys())
    counts = list(bmi_records.values())

    plt.bar(categories, counts, color=['blue', 'green', 'orange'])
    plt.xlabel('BMI Categories')
    plt.ylabel('Number of People')
    plt.title('Distribution of BMI Categories')
    plt.show()

if __name__ == "__main__":
    main()

