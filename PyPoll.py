#importing module 
import csv 
#short for directory
dir(csv)
#other useful modules 
# import random
# import numpy 

#DIRECT PATH TO FILE
#open a file; general format for opening a file is, file_variable = open(filename, mode)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Python has a way around open/close through using with
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# INDIRECT PATH TO FILE
# import os
# dir(os)
# Chaining to make multiple method calls on the same object 
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)