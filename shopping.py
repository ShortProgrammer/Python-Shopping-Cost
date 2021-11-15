#Shopping program
#Takes item names, prices, coupons, and tax
#Outputs cost

print ("Welcome to Shopping Costs")
i = 0
j = 0
nameList = []
priceList = []
while i != 1:
    nameList.append(input('Please enter name of item. Put 1 if you wish to exit: '))
    if nameList[j] == "1":
        i = 1
        nameList.remove("1")
    else:
        price = input('Please enter cost of item: ')
        while price.isdigit() != True:
            price = input('Please enter cost of item: ')
        price = float(price)
        priceList.append(price)
        j += 1

# for i in range (len(nameList)): #for testing to see what's in the list
#     print(nameList[i] + " $" + str(priceList[i]))

i = 0
j = 0
couponList = []
while i != 1:
    coupon = input('Please enter coupon worth. Enter DONE to stop: ')
    coupon = coupon.upper()
    if coupon == "DONE":
        i = 1
    else:
        while coupon.isdigit() != True:
            coupon = input('Please enter coupon worth: ')
        coupon = float(coupon)
        couponList.append(coupon)
        j+=1

# for i in range (len(couponList)): #for testing to see what's in the list
#     print(" $" + str(couponList[i]))

i = 0
while i != 1:
    tax = input('Please enter tax amount: ')
    try:
        float(tax)
        i = 1
    except ValueError:
        print ("Not a tax amount")

itemCost = 0.0
for i in range (len(priceList)): 
    itemCost = itemCost + priceList[i]

couponCost = 0.0
for i in range (len(couponList)): 
    couponCost += couponList[i]

print("item: " + str(itemCost) + " coupon: " + str(couponCost))

costBefore = float(itemCost - couponCost)
taxCost = costBefore * float(tax)

print("before: " + str(costBefore) + " tax: " + str(taxCost))

finalCost = round((costBefore + taxCost),2)

print("final: " + str(finalCost))
