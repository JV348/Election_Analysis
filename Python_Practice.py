print("Hello World!")
counties = ["Arapahoe", "Denver", "Jefferson"]
print("counties = ['Arapahoe','Denver'', 'Jefferson'] Initialized")
print("displaying index locations")
counties[0]
print(counties[0])
counties[2]
print(counties[2])
print(counties[-1])
len(counties)
print("len(counties) gives length of list")
counties[0:2] 
print("to find the first and second items from counties")
counties.append("El Paso")
print("added El Paso to the List")
counties.insert(2, "El Paso")
print("specifies where the new item is added in index")
print("counties.remove('ElPaso') would remove")
print("counties.pop(3) or pop(-1) would remove as well")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print("create a dictionary")
counties_dict 
print("display the dictionary created")
counties_dict.items()
print("keys and values displayed")
counties_dict.keys()
print("only keys displayed")
counties_dict.values()
print("only values displayed")
counties_dict.get("Denver")
counties_dict["Arapahoe"]
print("specific value displayed")

voting_data = []
print("creating an empty list for the list of dictionaries")
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#Decision Statements or Conditionals 
counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#else-if statement 
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#nested elsi-if statement
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade 
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

#Using the if-elif-else statement, rewrite the code and run the file
 # What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#Back to Elections - Membership Operators in/not 
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else: 
    print("El Paso is not in the list of counties.")

# Logical Operators and/or/not can be combined
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not is the list of counties.")

# For Loops 
#for item in [items]:
 #   statement 1
  #  statement 2
for county in counties:
    print(county)
#loop alternatively with range where i is used to indicate the index
for i in range(len(counties)):
    print(counties[i])
# loop through dictionary to get keys - two ways
for county in counties_dict: 
    print(county)
for county in counties_dict.keys():
    print(county)
# loop through dictionary to get values - two ways
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict.get(county))
# key-value pairs 
for county, voters in counties_dict.items():
    print(county, voters)

#loop/iterate through list of dictionaries 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
# alterative 
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
# get the values across dictionaries 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# f strings in python
#original code 
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
 #   print(county + " county has " + str(voters) + " registered voters.")
#modified code for f 
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")