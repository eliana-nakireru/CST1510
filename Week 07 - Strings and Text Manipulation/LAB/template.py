"""
RECORD CHECK  -  my version
===========================

Name  :Eliana Nakireru
Lane  : IT      (delete two)
Date  :7th November, 2026


Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


#1. Threshold

def parse_line(raw_line):
    """Return a clean line in form of a dict"""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)
    name = hostname_part.strip()
    remainder = rest.split(",")

    document = {"hostname": name}
    for r in remainder:
        key, value = r.split("=")
        value = value.strip()
        document[key.strip()] = float(value)
    return document

lines = ["srv-04, used = 87, Total=100",
         "SRV-05, used=50, total =150",
         "srv-06, Used = 90, total = 100",
         "Srv-07,UsEd=35, TotaL=60",
         "srv-08, USed=120, total=40"]

for l in lines:
    print(parse_line(l))
    print()







#2. Typical
def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK for used/total * 100."""
    percent = (used/total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def parse_line(raw_line):
    """Return a clean line in form of a dict"""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)
    name = hostname_part.strip()
    remainder = rest.split(",")

    document = {"hostname": name}
    for r in remainder:
        key, value = r.split("=")
        value = value.strip()
        document[key.strip()] = float(value)
           
    return document

for l in lines:
        document = parse_line(l)
        s = status_of(document["used"], document["total"])
        print(document["hostname"], s)







# 3. Excellent
count_of_records = 0
counts_flagged = 0

with open("eli'smessy_lines.txt", "r") as file:
    for raw_line in file:
        document = parse_line(raw_line)
        s = status_of(document["used"], document["total"])
        

        count_of_records += 1
        """Flag records with a status of "WARNING" & "OVER LIMIT."""
        if s != "OK":
         counts_flagged += 1


print()
print("Total No. of records:", count_of_records)
print("No. of flagged records:", counts_flagged)
    


