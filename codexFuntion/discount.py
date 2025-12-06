def apply_discount(discount_code, price, item_name):
    if discount_code.upper() == "SAVE10":
        price-=(price*0.1)
        print(price)
    elif discount_code.upper() == "HALFOFF":
        price-=(price*0.5)
        print(price)
    else:
        print("No valid code!")

apply_discount("SAVE100", 3000, "GBOGO")
