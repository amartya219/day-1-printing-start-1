print("Roller coaster Ride System")
height = float(input("Input Height: "))
if height > 1.5:
  print("You are eligible to ride")
  age = int(input("Input age: "))
  bill = 0
  if age < 12:
    print("Pay 5$")
    bill = 5
  if 12 < age < 17:
    print("Pay 7$")
    bill = 7
  if age > 18:
    print("pay 12$")
    bill = 12
  want_photos = input("Do you want photos? Press Y or N ")
  if want_photos == "Y":
    Total_bill = int(bill) + 3
    print(Total_bill)
  else:
   print(bill)
else:
    print("You are not eligible to ride")
