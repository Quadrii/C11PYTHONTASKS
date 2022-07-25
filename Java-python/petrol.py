from petrol_purchase import Petrol
#Constructor
MyPurchase = Petrol(0, "Ogba", "petrol", 0)

MyPurchase.quantity = int(input("How many liters of petrol did you buy: "))
qty = MyPurchase.quantity
print(qty)

MyPurchase.location = input("Enter name of filling station: ")
locatn = MyPurchase.location
print(locatn)

MyPurchase.petrol_type = input("Enter petrol type (Diesel, petrol, Kerosene): ")
pms_type = MyPurchase.petrol_type
print(pms_type)

MyPurchase.petrol_price = int(input("How much does a liter of " + MyPurchase.petrol_type + " " + " cost: "))
pms_price = MyPurchase.petrol_price
print(pms_price)

discount = int(input("Enter discount: "))
print(MyPurchase.net_purchase(discount))

print("The total price of ", MyPurchase.petrol_type , " you bought is: ", MyPurchase.purchase_amount())

