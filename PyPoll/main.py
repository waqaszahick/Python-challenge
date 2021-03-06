import os

# Defined relative path to read election_data.csv from the 'Resources folder
current_path = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(current_path, 'Resources//election_data.csv')

# Read the contents including total rows of election_data.csv
with open(my_file) as file:
    lines = file.readlines()
cand_list = []
cand_votes = []
total_votes = len(lines)-1

# Create 'analysis' folder and generate analysis_election_data.txt in 'analysis' folder
my_file_1 = os.path.join(current_path, 'analysis//analysis_election_data.txt')
file = open(my_file_1, 'w+')

# Display 'Election Results' heading and 'Total Votes' analysis output
print('\n')
print('Election Results')
print("-" * 25)
print('Total Votes: ', total_votes)
print("-" * 25)

# Display analysis output in analysis_election_data.txt in already generated analysis folder
file.write('Election Results \n' + ('-' * 30) + '\nTotal Votes: ' + str(total_votes) + '\n' + ('-' * 30) + '\n')

# Calculate 'total votes' and 'percentage of votes' for the candidates
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

# Display 'Winner' candidate results
print("-" * 25)
print('Winner: ', max_votes_candidate)

# Display 'Winner' candidate name in analysis_election_data.txt in already generated analysis folder
file.write(('-' * 30) + '\nWinner: ' + max_votes_candidate + '\n' + ('-' * 30))

print("-" * 25)
print('\n')

file.close()