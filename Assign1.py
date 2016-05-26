"""
CP1404 - Assignment 1 : 2016
Items For Hire
Kye Cook
Start Date - 29/03/2016
GitHub Repository Link : https://github.com/KyeCook
"""
import csv

FILE_NAME = "items.csv"
MENU = "Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"


def main():
    print("Welcome to the Items For Hire Program")
    print("Written by Kye Cook, March 2016")

    item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count = load_items()

    print(MENU)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            print("All items on file (* indicates item is currently out):")
            for line in items:
                print(line)

        elif menu_selection == "H":
            hire_items(item_id, item_names, item_availability, item_costs, items)
        elif menu_selection == "R":
            return_items(item_id, item_names, item_availability, item_costs, items)
        elif menu_selection == "A":
            add_items(item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count)
        else:
            print("Invalid Menu Choice")
        print(MENU)
        menu_selection = input(">>> ").upper()
    update_csv(item_names, item_descriptions, item_costs, item_availability, items)
    print("{} items saved to items.csv\nHave a nice day :)".format(len(item_id)))


def load_items():
    """
    Pseudocode:

    load items.csv document

    item_names = empty list
    item_descriptions = empty list
    item_cost = empty list
    item_availability = empty list
    item_id = empty list
    items = empty list
    count = -1

    for row in items.csv
        count = count + 1
        item_id = item_id + count
        item_names = item_names + row 1 of items.csv
        item_descriptions = item_descriptions + row 2 of items.csv
        item_cost = item_cost + row 3 of items.csv

        if row 4 of items.csv = "out"
            item_availability = item_availability + "*"
        else
            item_availability = item_availability + ""
        items = items + item_id, item_names, item_descriptions, items_cost, item_availability

    :return: items
    """

    f = open(FILE_NAME)
    csv_f = csv.reader(f)
    items = []

    item_id_count = -1

# Reads each row in items.csv and appends data to appropriate list.
    for row in csv_f:
        new_item = []

        new_item.append(row[0])
        new_item.append(row[1])
        new_item.append(float(row[2]))
        new_item.append(row[3])

        items.append(new_item)

    return items


def hire_items(item_id, item_names, item_availability, item_costs, items):
    """
    Pseudocode:

    :param items:
    :param item_id:
    :param item_names:
    :param item_costs:
    :param item_availability:
    valid_input = False

    for line in items
        if last value in line not = "*"
            display line
    display("Enter number of item to hire")
    while not valid_input
        get item_to_hire
        if item_to_hire is in first row of items
            last row of items = "*"
            item_availabilities = "*"
            display "Item hired"
            valid_input = True
            :return: items
        else
            display "Item not on hire"
    """
    valid_input = False
    in_count = 0

# Checks to see if last value within each row is a "*". This allows for only items that are 'in' to be displayed
    for line in items:
        if line[-1] != "*":
            in_count += 1
            print(line)
# Checks to see if any items are in stock. Returns to menu if no items available
    if in_count <= 0:
        print("No items are currently available for hire")
        return item_availability
    print("Enter number of item to hire")

    while not valid_input:
        # This statement error checks users input to ensure it is of a numerical value. Gives a generated error message
        # rather than python crash. Allows user to re-enter value until correct.
        try:
            item_to_hire = int(input(">>> "))
            if item_to_hire > (len(item_id) - 1):
                print("Invalid item number")
            elif item_to_hire in item_id and "*" not in items[item_to_hire]:
                item_availability[item_to_hire] = "*"

                items[item_to_hire] += '*'
                print("{} hired for ${}".format(item_names[item_to_hire], item_costs[item_to_hire]))

                valid_input = True

                return item_availability[item_to_hire]
            elif "*" in items[item_to_hire]:
                print("That item is not available for hire")
                return item_availability
            else:
                print("Invalid item number")
        except ValueError:
            print("Invalid input, enter a number")


def return_items(item_id, item_names, item_availability, item_costs, items):
    valid_input = False
    out_count = 0

# Checks to see if last value within each row is a "". This allows for only items that are 'out' to be displayed
    for line in items:
        if line[-1] == "*":
            out_count += 1
            print(line)
# Checks to see if any items are out of stock. Returns to menu if all items in stock
    if out_count <= 0:
        print("No items are currently on hire")
        return item_availability
    print("Enter number of item to return")

    while not valid_input:
        # This statement error checks users input to ensure it is of a numerical value. Gives a generated error message
        # rather than python crash. Allows user to re-enter value until correct.
        try:
            item_to_return = int(input(">>> "))
            if item_to_return > (len(item_id) - 1):
                print("Invalid item number")
            elif item_to_return in item_id and "*" in items[item_to_return]:
                item_availability[item_to_return] = ""

                items[item_to_return] = ("{} - {} = $ {}{}".format(item_id[item_to_return], item_names[item_to_return],
                                         item_costs[item_to_return], item_availability[item_to_return]))

                print(item_names[item_to_return], "returned")

                valid_input = True

                return item_availability[item_to_return]

            elif "*" not in items[item_to_return]:
                print("That item is not on hire")
                return item_availability
            else:
                print("Invalid item number")
        except ValueError:
            print("Invalid input, enter a number")


def add_items(item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count):
    valid_input = False
    item_id_count += 1
    item_id.append(item_id_count)

    item_availability.append("")
# Error Checking Loops - Ensure no empty values are entered
    item_names_new = (input("Item name:"))
    while item_names_new == "":
        print("Input can not be empty")
        item_names_new = (input("Item name:"))
    item_names.append(item_names_new)

    item_descriptions_new = (input("Description:"))
    while item_descriptions_new == "":
        print("Input can not be empty")
        item_descriptions_new = (input("Description:"))
    item_descriptions.append(item_descriptions_new)
# Try statement to allow user to change input if not in float(numeric) format
    while not valid_input:
        try:
            item_costs_new = (float(input("Price per day: $")))
            if item_costs_new < 0:
                print("Price must be >= $0")
            else:
                item_costs.append(item_costs_new)
                valid_input = True
        except ValueError:
            print("Enter a valid number")

    print("{} ({}), ${:.2f} now available for hire".format(item_names[item_id_count], item_descriptions[item_id_count],
                                                           item_costs[item_id_count]))

    items.append("{} - {} ({}) = $ {:>7.2f}{}".format(item_id[item_id_count], item_names[item_id_count],
                                                      item_descriptions[item_id_count], item_costs[item_id_count],
                                                      item_availability[item_id_count]))

    return items, item_names, item_costs, item_id_count, item_descriptions, item_availability


def update_csv(items):
    # # Needs to re-open file in new write format
    # f = open(FILE_NAME, 'w')
    # for item in items:
    #     f.write(','.join(str(part) for part in items) + '\n')
    # f.close()

    with open (FILE_NAME, "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerows(items)

    output.close()
# main()
