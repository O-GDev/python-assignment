price_table = """ 
     ----------------------------------------------------              
     |Pizza Type   |Number of Slices   |Price Per Box   |
     ----------------------------------------------------
     |Sapa Size    |4                  |2,000           |
     ----------------------------------------------------
     |Small Money  |6                  |2,400           |
     ----------------------------------------------------
     |Big Boys     |8                  |3,000           |
     ----------------------------------------------------
     |Odogwu       |12                 |4,200           |
     ----------------------------------------------------


"""

print(price_table)
number_of_people = int(input("Enter the number people: "))
pizza_type = input("What type of pizza do you want?: ").lower()
number_of_boxes_to_buy = 0
left_over=0
customer_cost=0
overall_slices = 0
price = 0

if pizza_type == "sapa size":
    number_of_boxes_to_buy=number_of_people//4
    if number_of_people%4 != 0:
        number_of_boxes_to_buy+=1
        left_over=4-number_of_people%4
        price=2000
    customer_cost=number_of_boxes_to_buy*price
    overall_slices = number_of_boxes_to_buy * 4
    


if pizza_type == "small money":
    number_of_boxes_to_buy=number_of_people//6
    if number_of_people%6 != 0:
        number_of_boxes_to_buy+=1
        left_over=6-number_of_people%6
        price=2400
    customer_cost=number_of_boxes_to_buy*price
    overall_slices = number_of_boxes_to_buy * 6


if pizza_type == "big boys":
    number_of_boxes_to_buy=number_of_people//8
    if number_of_people%8 != 0:
        number_of_boxes_to_buy+=1
        left_over=8-number_of_people%8
        price=3000
    customer_cost=number_of_boxes_to_buy*price
    overall_slices = number_of_boxes_to_buy * 8


if pizza_type == "odogwu":
    number_of_boxes_to_buy=number_of_people//12
    if number_of_people%12 != 0:
        number_of_boxes_to_buy+=1
        left_over=12-number_of_people%12
        price=4200
    customer_cost=number_of_boxes_to_buy*price
    overall_slices = number_of_boxes_to_buy * 12

{left_over}
print(f"Number of boxes of pizza to buy = {number_of_boxes_to_buy} boxes (explanation: Odogwu size contains 12 slice per box, {number_of_boxes_to_buy} boxes should be sufficient for {number_of_people} people as it would contain {overall_slices} slices in all). Number left over slice after serving = {left_over} slices (explanation : After serving {number_of_people} slices, you should have {left_over} slices left) Prices = {customer_cost} (explanation : {price} per box for {number_of_boxes_to_buy} boxes")
