import math

# **********************************************************************************************************************
# The boss ordered the employee to fill 330 ml bottles with liquid in such a way that 12% of the bottle was empty.
# The employee made an agreement with the boss that he could leave all the liquid that would remain for him and would
# not be enough to fill the bottles. After take-off, receive information from the user how many ml of fluid was supplied
# by the factory, and the result should be the amount of liquid that the employee will be able to take with him :)
# **********************************************************************************************************************

# DATA

# bottles size = 330ml
# filling the bottle = 88% of their capacity

# input >>>>>>>  how much liquid was delivered to the bottling plant?
# output >>>>>>  how many bottles are needed to spill the liquid provided
# output >>>>>>  how much fluid will be left for the employee

# units
# liquid 1 liter
# the capacity of the bottles will be calculated in liters

amount_of_liquid = float(input("Podaj ilość cieczy w litrach przeznaczonej do rozlania \n"))

bottle_size = 0.33
bottle_empty_space = 0.12
bottle_liquid_amount = 1 - bottle_empty_space  # the amount of liquid poured into the bottle in "%"

filling_quantity = bottle_size * bottle_liquid_amount
filling_quantity_output = round(filling_quantity, 2)
bottles_number = (math.floor(amount_of_liquid / filling_quantity))

used_liquid = bottles_number * filling_quantity
remaining_liquid = amount_of_liquid - used_liquid
liquid_for_employee = remaining_liquid

print(f"Ilość cieczy do rozlania to: {amount_of_liquid}l")
print(f"Do każdej butelki zostanie wlane {filling_quantity_output}l cieczy")
print(f"do rozlania {amount_of_liquid}l cieczy będą potrzebne {bottles_number} butelki")
print(f"ilość zużytej cieczy to: {used_liquid:.2f}l")
print(f"pozostała ciecz to: {remaining_liquid:.2f}l.")
print(f"Pracownik może zabrać ze sobą {liquid_for_employee:.2f}l płynu")
