print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("Ho much tip would you like to give? 10, 12, or 15? "))
nb_people = int(input("How many people to split the bill? "))

bill_per_person = total_bill / nb_people
tip_in_percentage = tip / 100
resultat = round(bill_per_person + (bill_per_person*tip_in_percentage), 2)
print(f"Each person should pay: ${resultat}")
