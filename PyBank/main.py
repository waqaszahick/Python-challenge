import os
current_path = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(current_path, 'Resources//budget_data.csv')

with open(my_file) as file:
    lines = file.readlines()
    total_month = (len(lines)-1)
    net_total = 0
    changes = []

    previous_month = int(lines[1].split(",")[1].strip())
    months = []
    for line in lines[1:]:
        months.append(line.split(',')[0])
        line = line.split(",")[1].strip()
        net_total = net_total + int(line)

        change = int(line) - previous_month
        previous_month = int(line)
        changes.append(change)

    total_change = sum(changes)
    average_change = round(total_change/(total_month-1), 2)
    max_change = max(changes)
    max_change_month = months[changes.index(max_change)]
    min_change = min(changes)
    min_change_month = months[changes.index(min_change)]

my_file_1 = os.path.join(current_path, 'analysis//analysis_budget_data.txt')

file = open(my_file_1,'w+')

print('\n')
print("-" * 50)
print('Financial Analysis')
print("-" * 50)
print('Total Months: ', total_month)
print('Total: $', net_total)
print('Average Change: $', average_change)
print('Greatest Increase in Profits: {} (${})'.format(max_change_month, max_change))
print('Greatest Decrease in Profits: {} (${})'.format(min_change_month, min_change))
print("-" * 50)
print('\n')

file.write('Financial Analysis \n\n Total Months: ' + str(total_month) + '\n Total: $' + str(net_total) + '\n Average Change: $' + str(average_change) + '\n Greatest Increase in Profits: {} (${})'.format(max_change_month, max_change) + '\n Greatest Decrease in Profits: {} (${})'.format(min_change_month,min_change))
file.close()