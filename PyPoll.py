#open a file; general format for opening a file is, file_variable = open(filename, mode)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Python has a way around open/close through using with
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


# Add our dependencies.
import csv
dir(csv)
import os
dir(os)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file alternative and separate into lines using newline escape sequence "n"
     txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    #Raad the file object with the reader function 
    file_reader = csv.reader(election_data)

    # Print the header row 
    headers = next(file_reader)
    print(headers)