from typing import Counter


class cal():

    def calculation(x):
        return x
    
    def monetaryValue(m):
        if 500001<=m and m<=100000000000000:
            return "Extremely High"
        elif 100001<=m and m<=500000:
            return "High"
        elif 10001<=m and m<=100000:
            return "Significant"
        elif 1001<=m and m<=10000:
            return "Minor"
        elif 1<=m and m<=1000:
            return "Insignificant"
        else:
            return "unknown"

    def consequence(c, mon):

        if c == "Tolerable" and mon == "Insignificant":
            return "Insignificant"
        elif c == "Tolerable" and mon == "Minor":
            return "Insignificant"
        elif c == "Tolerable" and mon == "Significant":
            return "Low"
        elif c == "Tolerable" and mon == "High":
            return "Major"
        elif c == "Tolerable" and mon == "Extremely High":
            return "Severe"

        elif c == "Reversible" and mon == "Insignificant":
            return "Insignificant"
        elif c == "Reversible" and mon == "Minor":
            return "Low"
        elif c == "Reversible" and mon == "Significant":
            return "Moderate"
        elif c == "Reversible" and mon == "High":
            return "Severe"
        elif c == "Reversible" and mon == "Extremely High":
            return "Severe"

        elif c == "costly" and mon == "Insignificant":
            return "Low"
        elif c == "costly" and mon == "Minor":
            return "Moderate"
        elif c == "costly" and mon == "Significant":\
            return "Major"
        elif c == "costly" and mon == "High":
            return "Severe"
        elif c == "costly" and mon == "Extremely High":
            return "Severe"

        elif c == "Unreversible" and mon == "Insignificant":
            return "Moderate"
        elif c == "Unreversible" and mon == "Minor":
            return "Major"
        elif c == "Unreversible" and mon == "Significant":
            return "Severe"
        elif c == "Unreversible" and mon == "High":
            return "Severe"
        elif c == "Unreversible" and mon == "Extremely High":
            return "Severe"

        else:
            return "unknown"
    
    def controlLayer(a,b,c,d,e):
        counter = 0
        if a == "AV":
            counter +=1
        if b == "AV":
            counter += 1
        if c == "AV":
            counter += 1
        if d == "AV":
            counter += 1
        if e == "AV":
            counter += 1
        return counter



    def likelihood(cl, f):

        if cl == 0 and f == "Daily":
            return "Certain"
        elif cl == 0 and f == "Weekly":
            return "Certain"
        elif cl == 0 and f == "Monthly":
            return "Likely"
        elif cl == 0 and f == "Quarterly":
            return "Possible"
        elif cl == 0 and f == "Semi Anually":
            return "Unlikely"
        elif cl == 0 and f == "Anually":
            return "Unlikely"

        elif cl == 1 and f == "Daily":
            return "Certain"
        elif cl == 1 and f == "Weekly":
            return "Certain"
        elif cl == 1 and f == "Monthly":
            return "Possible"
        elif cl == 1 and f == "Quarterly":
            return "Unlikely"
        elif cl == 1 and f == "Semi Anually":
            return "Unlikely"
        elif cl == 1 and f == "Anually":
            return "Rare"
        
        elif cl == 2 and f == "Daily":
            return "Likely"
        elif cl == 2 and f == "Weekly":
            return "Possible"
        elif cl == 2 and f == "Monthly":
            return "Unlikely"
        elif cl == 2 and f == "Quarterly":
            return "Unlikely"
        elif cl == 2 and f == "Semi Anually":
            return "Rare"
        elif cl == 2 and f == "Anually":
            return "Rare"

        elif cl == 3 and f == "Daily":
            return "Possible"
        elif cl == 3 and f == "Weekly":
            return "Unlikely"
        elif cl == 3 and f == "Monthly":
            return "Unlikely"
        elif cl == 3 and f == "Quarterly":
            return "Rare"
        elif cl == 3 and f == "Semi Anually":
            return "Rare"
        elif cl == 3 and f == "Anually":
            return "Rare"
        
        elif cl == 4 and f == "Daily":
            return "Unlikely"
        elif cl == 4 and f == "Weekly":
            return "Unlikely"
        elif cl == 4 and f == "Monthly":
            return "Rare"
        elif cl == 4 and f == "Quarterly":
            return "Rare"
        elif cl == 4 and f == "Semi Anually":
            return "Rare"
        elif cl == 4 and f == "Anually":
            return "Rare"
        
        elif cl == 5 and f == "Daily":
            return "Unlikely"
        elif cl == 5 and f == "Weekly":
            return "Rare"
        elif cl == 5 and f == "Monthly":
            return "Rare"
        elif cl == 5 and f == "Quarterly":
            return "Rare"
        elif cl == 5 and f == "Semi Anually":
            return "Rare"
        elif cl == 5 and f == "Anually":
            return "Rare"       
        else:
            return "unknown"       

    def riskLevel(c, l):
        if c == "Insignificant" and l == "Rare":
            return 1
        elif c == "Insignificant" and l == "Unlikely":
            return 1
        elif c == "Insignificant" and l == "Possible":
            return 1
        elif c == "Insignificant" and l == "Likely":
            return 1
        elif c == "Insignificant" and l == "Certain":
            return 2

        elif c == "Low" and l == "Rare":
            return 1
        elif c == "Low" and l == "Unlikely":
            return 1
        elif c == "Low" and l == "Possible":
            return 1
        elif c == "Low" and l == "Likely":
            return 2
        elif c == "Low" and l == "Certain":
            return 3
        
        elif c == "Moderate" and l == "Rare":
            return 1
        elif c == "Moderate" and l == "Unlikely":
            return 1
        elif c == "Moderate" and l == "Possible":
            return 2
        elif c == "Moderate" and l == "Likely":
            return 3
        elif c == "Moderate" and l == "Certain":
            return 4
        
        elif c == "Major" and l == "Rare":
            return 1
        elif c == "Major" and l == "Unlikely":
            return 2
        elif c == "Major" and l == "Possible":
            return 3
        elif c == "Major" and l == "Likely":
            return 4
        elif c == "Major" and l == "Certain":
            return 5
        
        elif c == "Severe" and l == "Rare":
            return 2
        elif c == "Severe" and l == "Unlikely":
            return 3
        elif c == "Severe" and l == "Possible":
            return 4
        elif c == "Severe" and l == "Likely":
            return 5
        elif c == "Severe" and l == "Certain":
            return 5
        else:
            return 666

    def totalScore(x):
        counter = 0
        for i in x:
            if i.unrectified_Audit_Findings and i.level and i.level!=666:
                counter += i.unrectified_Audit_Findings * i.level   
        return counter
    def grade(x):
        if x > 50:
            return "Top Priority"
        elif x > 40 and x <= 50:
            return "Critical For Review"
        elif x > 30 and x <= 40:
            return "Important To Tackle"
        elif x > 20 and x <= 30:
            return "Lower Priority"
        elif x > 0 and x <= 20:
            return "Audit Probably Unnecessary"
        else:
            return "Unknown"
        
        