import os
import csv


csv_input_path = os.path.join("Resources", "election_data.csv")
txt_output_path = os.path.join("../03--Outputs", "poll_output.txt")

voter_id = []
county = []
electable_name = []

dict_4_votes = {}
voter_id_xref = {}

total_votes = 0

voter_fraud_count = 0
possibly_invalid_votes = 0
corrected_vote_total = 0

winning_vote_total = 0
winning_name = ""


with open(csv_input_path, mode = "r") as poll_data:

    csv_reader = csv.reader(poll_data, delimiter=',')

    ignore_header = next(csv_reader)

    initial_data = next(csv_reader)

    voter_id = initial_data[0]
    county = initial_data[1]
    electable_name = initial_data[2]

    
    for row in csv_reader:

        voter_id = row[0]
        county = row[1]
        electable_name = row[2]


        if voter_id in voter_id_xref:

            total_votes = total_votes + 1

            voter_fraud_count = voter_fraud_count + 1

            possibly_invalid_votes = possibly_invalid_votes + 1

            electable_name = "fraudulent vote"
            
            dict_4_votes[electable_name] = dict_4_votes[electable_name] + 1


        if voter_id not in voter_id_xref:
            
            voter_id_xref[voter_id] = int(row[0])

            total_votes = total_votes + 1

            corrected_vote_total = corrected_vote_total + 1


            if electable_name not in dict_4_votes:
            
                dict_4_votes[electable_name] = 0

                dict_4_votes[electable_name] = dict_4_votes[electable_name] + 1
        

            if electable_name in dict_4_votes:

                dict_4_votes[electable_name] = dict_4_votes[electable_name] + 1


#============================================================
#=================TERMINAL & TXT OUTPUT SCRIPT===============
#============================================================

print_string = (
    f"-------------------------------------------------------------\n"
    + f"ELECTION RESULTS\n"    
    + f"-------------------------------------------------------------\n"
    + f"Total Votes: {total_votes}\n"
    + f"Voter Fraud Count: {voter_fraud_count}\n"
    + f"Further Invalidated Votes Tally: {possibly_invalid_votes}\n"
    + f"Corrected Votes Count: {corrected_vote_total}\n"
    + f"-------------------------------------------------------------\n")

for key, value in dict_4_votes.items():

    vote_percent = (value) / (total_votes) * 100

    print_string = (
        print_string
        + f"{key}: %3.3f%% ({value} votes)\n" % (float(value) / float(total_votes) * 100))

    if value > winning_vote_total :

        winning_vote_total = value

        winning_name = key


print_string = (
    print_string
    + "=========================\n"
    + f"Winner: {winning_name}\n"
    + "========================="
    )

print(print_string)


with open(txt_output_path, "w") as txt_file:
    txt_file.write(print_string)