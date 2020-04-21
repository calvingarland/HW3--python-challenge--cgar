import os
import csv


csv_input_path = os.path.join("Resources", "budget_data.csv")
txt_output_path = os.path.join("../03--Outputs", "budget_output.txt")

month_list_change = []
pl_list_change = []

total_months = 0
new_pl = 0
old_pl = 0
delta_pl = 0
total_pl = 0

max_delta_inc = 1
mdi_id = ""

max_delta_dec = -1
mdd_id = ""

delta_avg = 0

x = 0
n = 0
l = 0


with open(csv_input_path, mode = "r") as budget_data:

    csv_reader = csv.reader(budget_data, delimiter=',')

    ignore_header = next(csv_reader)

    initial_data = next(csv_reader)

    total_months = total_months + 1

    new_pl = int(initial_data[1])

    total_pl = total_pl + int(initial_data[1])

    old_pl = int(initial_data[1])



    for row in csv_reader:

        total_months = total_months + 1

        delta_pl = int(row[1]) - old_pl

        old_pl = int(row[1])

        total_pl = total_pl + int(row[1])

        pl_list_change = pl_list_change + [delta_pl]

        x = int(delta_pl)

        if  x > max_delta_inc:
            max_delta_inc = int(row[1])
            mdi_id = row[0]

        if  x < max_delta_dec:
            max_delta_dec = int(row[1])
            mdd_id = row[0]


n = sum([delta_pl])

l = len([delta_pl])

delta_avg = n / l

#============================================================
#=================TERMINAL & TXT OUTPUT SCRIPT===============
#============================================================

#TERMINAL OUTPUT
print(f'===============================================\n')
print(f'Financial Analysis\n')
print(f'===============================================\n')
print(f'Total Months: {total_months}\n')
print(f'Total: {total_pl:10.2f}\n')
print(f'Average Change: (${delta_avg:10.2f})\n')
print(f'Greatest Increase in Profits: {mdi_id} ($%10.2f)\n' % (max_delta_inc))
print(f'Greatest Decrease in Profits: {mdd_id} ($%10.2f)\n' % (max_delta_dec))

#TXT FILE OUTPUT
with open(txt_output_path, "w") as text_file:
    text_file.write(f'=================================================\n')
    text_file.write(f'Financial Analysis\n')
    text_file.write(f'=================================================\n')
    text_file.write(f'Total Months: {total_months}\n')
    text_file.write(f'Total: {total_pl:10.2f}\n')
    text_file.write(f'Average Change: (${delta_avg:10.2f})\n')
    text_file.write(f'Greatest Increase in Profits: {mdi_id} ($%10.2f)\n' % (max_delta_inc))
    text_file.write(f'Greatest Decrease in Profits: {mdd_id} ($%10.2f)\n' % (max_delta_dec))


