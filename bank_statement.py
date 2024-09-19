import csv
from re import sub
from datetime import date

# credit_card_file = input("Enter the file name: ")
# month = int(input("Enter the month: "))
month = 9

def get_date_obj(date_string):
    date_list = date_string.split("/")
    if date_list[0] == 'Date':
        return date(1996, 8, 5)

    # Check to see if month has 2 digits
    if len(date_list[0]) == 1:
        date_list[0] = "0" + date_list[0]

    # Dates are formated m/d/y
    return date(int(date_list[2]), int(date_list[0]), int(date_list[1]))

def create_summary_file(categories, total):
    file_name = "spend_categories.txt"
    with open(file_name, "w") as file:
        file.write("Total Spent: $" + str(total) + "\n\n")
        for category, amount in categories.items():

            file.write(category + ": $" + str(amount) + " \n")

spend_categories = {}
total_spent = 0

with open('creditCardAccountActivityExport.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # ignore the first row
    next(reader)

    for row in reader:
        current_date = get_date_obj(row[0])
        print(current_date, row)
        if current_date.month == month and current_date.year > 2023:
            current_category = row[4]
            print(current_category)
            if current_category == "" or current_category == "-":
                current_category = "Misc"

            # Remove everything but numbers and decimals
            amount = sub('[^0-9,.]','', row[2])
            if amount != '':
                amount = float(amount)
                # print(amount, current_category, reader.line_num)
                spend_categories[current_category] = round(spend_categories.get(current_category, 0) + amount, 2)

                total_spent += amount

total_spent = round(total_spent, 2)


create_summary_file(spend_categories, total_spent)