pizza_rate = 500
extra_toppings = 80
soft_drinks = 45
delivery_charge = 50

order_items = 2 * pizza_rate + 1 * extra_toppings + 3 * soft_drinks

delivery = order_items + delivery_charge

gst_rate = delivery * .18

total_rate = delivery + gst_rate 

print (total_rate)



############################################

print('----------Menu-----------\n Pizza Rate = 500 \n Extra Toppings = 80 \n Soft Drinks = 50 \n ------------------------')

pizza = int(input('Pizza :'))
toppings = int(input('Extra Toppings :'))
softDrinks = int(input('Soft Drinks :'))


total = (pizza*pizza_rate + toppings*extra_toppings + softDrinks*soft_drinks + delivery_charge) + (pizza*pizza_rate + toppings*extra_toppings + softDrinks*soft_drinks + delivery_charge) * .18 

print('Your Bill is',total)

