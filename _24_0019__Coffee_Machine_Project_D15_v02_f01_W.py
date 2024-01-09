
#logo?

#start here:
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

#money cost (* 100)
espresso_cost_per_serving = 150
latte_cost_per_serving = 250
cappuccino_cost_per_serving = 300


#General Starting resources: (in ml, ml, and g grams)
Water_starting_resources = 300
Milk_starting_resources = 200
Coffee_starting_resources = 100

#Espresso resource usage
water_resourse_usage_amount_for_espresso = 50
coffee_resourse_usage_amount_for_espresso = 18
enough_espresso_resources = ""

#Latte resource usage
water_resourse_usage_amount_for_latte = 200
milk_resourse_usage_amount_for_latte = 150
coffee_resourse_usage_amount_for_latte = 24

#Cappuccino resource usage
water_resourse_usage_amount_for_cappuccino = 250
milk_resourse_usage_amount_for_cappuccino = 100
coffee_resourse_usage_amount_for_cappuccino = 24

user_drink_selection = input(f"Hello, welcome to Drinky Smort. What would you like to order? (e = espresso, l = latte, c = cappuccino): ").lower()

def check_inventory_levels_espresso():
    global continue_playing
    continue_playing = True
    while continue_playing:
        global Water_starting_resources, Milk_starting_resources, Coffee_starting_resources
        print(f"The current inventory levels - Water is at: {Water_starting_resources} ml\n Milk is at: {Milk_starting_resources} ml\n Coffee is at: {Coffee_starting_resources} g")
        current_water_resource_level = Water_starting_resources #minus other math...
        current_milk_resource_level = Milk_starting_resources #minus other math...
        current_coffee_resource_level = Coffee_starting_resources #minus other math...

        if water_resourse_usage_amount_for_espresso < Water_starting_resources and coffee_resourse_usage_amount_for_espresso < Coffee_starting_resources:
            enough_espresso_resources = True
        else:
            print("Sorry, not enough resources for this item")
            break



#####################################################################################

# Drink and Money transaction
if user_drink_selection == "e":
    print(f"That will cost ${espresso_cost_per_serving / 100:.2f}")
    print(f"Please insert coins:")
    pennies_entered_for_espresso = int(input(f"Quantity of pennies you will place in the machine: "))     #YOU NEEDED INT AND * 100 in certain areas, to get the math to work.
    nickels_entered_for_espresso = int(input(f"Quantity of nickels you will place in the machine: "))
    dimes_entered_for_espresso = int(input(f"Quantity of dimes you will place in the machine: "))
    quarters_entered_for_espresso = int(input(f"Quantity of quarters you will place in the machine: "))

    total_in_pennies = pennies_entered_for_espresso * penny # * 100
    print(f"${total_in_pennies:.2f} in pennies.")                                          #this gives you 2 decimal points  :.2f}")
    total_in_nickels = nickels_entered_for_espresso * nickel # * 100
    print(f"${total_in_nickels:.2f} in nickels.")
    total_in_dimes = dimes_entered_for_espresso * dime # * 100
    print(f"${total_in_dimes:.2f} in dimes.")
    total_in_quarters = quarters_entered_for_espresso * quarter # * 100
    print(f"${total_in_quarters:.2f} in quarters.")

    total_of_all_inserted_coins = ((total_in_pennies + total_in_nickels + total_in_dimes + total_in_quarters))
    print(f"The total you entered was ${total_of_all_inserted_coins:.2f}")

    print(f"The total for the drink costs ${espresso_cost_per_serving / 100:.2f}")
    change_difference_math = total_of_all_inserted_coins - (espresso_cost_per_serving/100)
    if change_difference_math < 0:
        print(f"Sorry, you don't have enough change to pay for this right now. You have been refunded ${total_of_all_inserted_coins:.2f}")
    elif change_difference_math > 0 and enough_espresso_resources == True:
        print(f"Enjoy your drink and your ${change_difference_math:.2f}!")
    # else:
        # check to see if we have enough coffee resources


# elif for latte

# elif for cappuccino


# TODO Program Requirements: # 1. Be able to Print a report (report what it has left inside the machine, resource-wise)

# TODO Program Requirements: # 2. Check if there’s sufficient resources.

# TODO Program Requirements: # 3. Process coins.

# TODO Program Requirements: # 4. Check if transaction successful. (enough money to cover the transaction)

# TODO Program Requirements: # 5. If successful, make coffee (deduct the resources)


while True:
    check_inventory_levels_espresso()
    play_again_option = input(f"Do you want to play again? (Y or N): ").upper()
    if play_again_option != "Y":
        break