#Self Reflection Questions
#1. The first bug I noticed was the missing colon at the end of the for loop. I found the other 2 through AI. I feel like I am okay at seeing the code. If I tried harder to completely fix it, I probably would have found it on my own.
#2. It calculates and applies a discount to the price on a customer's loyalty tier. They should be able to easily.
#3. # AI Assistance Disclosure:
# Portions of this lab's logic and debugging were assisted by an AI coding assistant. 
# The underlying concepts, implementation decisions, and final code were reviewed and verified by the author.


#---Exercise 1----

#Define calculate tax function

def calculate_tax(price,rate):
    return price * rate

#Calling function

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250,0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}") #$7.00
print(f"Tax on 250 at 8%: ${tax2:.2f}") #$20.00
print(f"Another Tax: ${calculate_tax(150,0.05):.2f}") #$7.50

#---Exercise 2---

def apply_discount(price,tier):
    if tier == "gold":
        return price * .85
    elif tier == "silver":
        return price * .90
    elif tier == "bronze":
        return price * .95
    else:
        return price

#Calling the function

price = 200
tiers = ["gold","silver","bronze","none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

#---Exercise 3---

#Write it out manually first, then refactor into a function
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

#Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}")

#---Exercise 4---

orders = [(200, "gold", 0.07), (150, "silver", 0.08), (80, "bronze", 0.05), (500, "none", 0.06)]

for price, tier, tax_rate in orders:
    total = final_price(price, tier, tax_rate)
    print(f"Price: ${price:.2f}, Tier: {tier}, Total: ${total:.2f}")

#---Exercise 5---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #adding the + makes it so they are not added together.
print(f"Total: ${total}")

count = 0
for sale in sales: #for loops need a colon at the end of the line to work properly. Helps with indentation.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #the index returned error because it was trying to access an index that was out of range. Changed the <= to < so it would not go out of range. Stop at 4 and not go to 5
    print(sales[i])
    i += 1


#---Exercise 6---

x = 100 #apple  #Global variable

def double_it():
    global x
    x = 999 #another apple(not same apple as above)
    return x * 2

print(x)
print(double_it())
print(x)