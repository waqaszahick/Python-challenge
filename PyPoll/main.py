import os

current_path = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(current_path, 'Resources//election_data.csv')

with open(my_file) as file:
    lines = file.readlines()
cand_list = []
cand_votes = []
total_votes = len(lines)-1

my_file_1 = os.path.join(current_path, 'analysis//analysis_election_data.txt')
file = open(my_file_1, 'w+')

print('\n')
print('Election Results')
print("-" * 25)
print('Total Votes: ', total_votes)
print("-" * 25)
file.write('Election Results \n\nTotal Votes: ' + str(total_votes) + '\n')
for line in lines[1:]:
    line_cs = line[0:-1].split(',')
    if not line_cs[2] in cand_list:
        cand_list.append(line_cs[2])
        cand_votes.append(1)
    else:
        index = cand_list.index(line_cs[2])
        cand_votes[index] += 1
per = []
j = 0
for votes in cand_votes:
    per.append(round(votes / total_votes * 100, 3))
    print('{}: {:.3f}% ({})'.format(cand_list[j], per[-1], cand_votes[j]))    
    file.write('{}: {:.3f}% ({}) \n'.format(cand_list[j], per[-1], cand_votes[j]))
    j += 1

max_per = max(per)
ind_max_per = per.index(max_per)
max_votes_candidate = cand_list[ind_max_per]
max_no_votes = cand_votes[ind_max_per]
print("-" * 25)
print('Winner: ', max_votes_candidate)
file.write('\n Winner: ' + max_votes_candidate)
print("-" * 25)
print('\n')
file.close()