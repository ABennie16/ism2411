#Reflection
#1. What is most surprising to me is that you can not edit the lists directly. You have to use certain remove or append to change it.
#2. In school, I had to report times of 40 yard dashes. It was hard to manually input all the data. It would've been easier had it been automated.

print("--- Exercise 1: Build the List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Add an Item ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("--- Exercise 4: Modifying a List ---")
inventory.append("envelope")
inventory.append("tape")
print(inventory)
inventory.remove("tape")
print(inventory)

inventory.sort()    
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.006)

try:
    coords[0] = 9
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident")

print(coords)

print("--- Exercise 6: Average of a List of Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulating Pattern ---")

prices = [9.99,14.99,4.99,24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")


