height = float(input("What is your height? \n"))
weight = float(input("What is your weight? \n"))

bmi = (weight / height ** 2)

round_bmi = round(bmi)

if round_bmi < 18.5 :
  print(f"You are underweight cuz your BMI is {round_bmi}. so Go and eat")
elif round_bmi >= 18.5 and round_bmi <= 24.9:
  print(f"You have normal BMI that is {round_bmi}. so Be happy!")
elif round_bmi >= 25 and round_bmi <= 29.9:
  print(f"You are overweight as your BMI is {round_bmi}. so Go to GYM!")
elif round_bmi >= 30:
  print(f"You have obesity as your BMI is {round_bmi}. so Go to GYM or you gonna die!")
