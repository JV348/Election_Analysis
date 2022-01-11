# Election Analysis Using Python

## Project Overview 
A client who works for the Colorado Board of Elections has tasked us with auditing a local election to determine the outcome and associated statistics.

1. Calculate the total number of votes cast. 

    The total number of votes cast was 369,711 ballots for the US Congressional precinct in Colorado.

2. Get a complete list of candidates who recieved votes.

    The candidates for the election cycle were:
    Charles Casper Stockham
    Diana DeGette
    Raymon Anthony Doane

3. Calculate the total number of votes each candidate recieved. 

    Each candidate had the following vote count:
    Charles Casper Stockham: (85,213)
    Diana DeGette: (272,892)
    Raymon Anthony Doane: (11,606)

4. Calculate the percentage of votes each candidate won.

    Each candidate had the following percentage of votes:
    Charles Casper Stockham: 23.0% 
    Diana DeGette: 73.8% 
    Raymon Anthony Doane: 3.1% 

5. Determine the winner of the election based on popular vote.

    According to the popular vote, the winner of the election was Diana DeGette - as she recieved 272,892 votes (a clear majority).

### Resources 
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code, 1.38.1

### Summary 
The analysis of the election shows that:
- There were 369,711 votes cast in the election. These were split amongst the three candidates.
    - Charles Casper Stockham: 85,213
    - Diana DeGette: 272,892
    - Raymon Anthony Doane: 11,606
- The candidate results were as follows:
    - Charles Casper recieved 23.0% of the vote and 85,213 votes. 
    - Diana DeGette recieved 73.8% of the vote and 272,892 votes. 
    - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette who recieved the majority with 73.8% of the vote or 272,892 counted votes.



## Challenge Overview 

## Overview of Election Audit
The election commission has requested additional data on voter turnout in the surrounding counties. We will return information regarding the voter turnout of each county, percentages of votes, and the county with the highest turnout. 

### Election-Audit Results:
- How many votes were cast in this congressional election?

    Overall, the total votes casted in this election were 381,711.

- Provide a breakdown of the number of votes and    the percentage of total votes for each county in the precinct.

    Those 381,711 votes were distributed amongst three surrounding counties, Jefferson, Denver and Arapahoe. According to the analysis, Jefferson County accounted for 38,855 votes or 10.5%; while Arapahoe County brought in 24,801 votes or 6.7%. On the other hand, Denver County amassed 306,055 votes or 82.8%.

- Which county had the largest number of votes?

    As noted prevously, Denver County definitely obtained the most votes for this election cycle.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

    Of the 381,711 votes casted, Stockham recieved 85,213, Doane recieved 11,606, and DeGette recieved 272,892 (with their respective percentages at 23%, 3.1%, and 73.8%).

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

    Diana DeGette was the winner of this election cycle, as she recieved 272,892 out of 381,711 votes (or 73.8% percent of total votes).


![First_segment](https://github.com/JV348/Election_Analysis/blob/3b461b83bb2548a4eb7385f5f617f6af479691b7/Resources/1_2.png)

![Second_segment](https://github.com/JV348/Election_Analysis/blob/3b461b83bb2548a4eb7385f5f617f6af479691b7/Resources/3_5.png)

![Third_segment](https://github.com/JV348/Election_Analysis/blob/3b461b83bb2548a4eb7385f5f617f6af479691b7/Resources/6_8.png)

![Election_analysis](https://github.com/JV348/Election_Analysis/blob/3b461b83bb2548a4eb7385f5f617f6af479691b7/Resources/election_analysis.png)


### Election-Audit Summary: Regarding Future Use
In retrospect, the code used for this analysis has come a long way and seen multiple iterations towards efficiency. It would be a shame to lay it to waste instead of finding further use for it. There are useful patterns involved that can be used again; in fact, there are notable similarities between the code used for county votes and the code used for candidate votes. 
With simple modifications, this code could be refactored and reused for another election. Of course, we intend to market this analyis to the commission and all counties in Colorado for future election cycles (which would entail new candidates and county votes). Aside from that, future iterations could be used for larger datasets such as city and state voting data. Furthermore, other variables, such as dates or poll locations, can be added to the analysis script with little problem - so as to increase the possible use.  

