import random

shopping_Items=["apples","Book","pizza","pc",1200,12.34,True]

#accessing the last item in the list by calculating its index
print(shopping_Items[len(shopping_Items)-1])

#accessing the last item in the list by its index (-1)
print(shopping_Items[-1])

#Adding a new item to the list

shopping_Items.append("Max")
print(shopping_Items)

#get random numbers
marks = []
for i in range(20):
    r = random.randint(0,100)
    marks.append(r)
print(marks)
above70 = []
between31_69 = []
below30 = []

''''
if marks[1]<31:
    below30.append(marks[1])


elif marks[1]>30 and marks[1]<70:
    between31_69.append(marks[1])

elif marks[1]>69:
    above70.append()

#comparing items of the list
'''

for item in marks:
    if item<31:
        below30.append(item)
    elif item>30 and item<70:
        between31_69.append(item)
    elif item>69:
        above70.append(item)

print(marks)
print(above70)
print(between31_69)
print(below30)