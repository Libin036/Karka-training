pizza_rate = 500
extra_toppings = 80
soft_drinks = 45
delivery_charge = 50

gst_rate = (pizza_rate + extra_toppings + soft_drinks + delivery_charge) * .18

total_rate = pizza_rate + extra_toppings + soft_drinks + delivery_charge + gst_rate

print(total_rate)

