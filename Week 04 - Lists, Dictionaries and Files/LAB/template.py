"""
RECORD CHECK  -  my version
===========================

Name  : Eliana Nakireru
Lane  :   IT      
Date  : 17th october, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# 1.
def check_record(value, limit):
    """Calculates what is required in the record"""
    difference = value - limit
    percentage = (value/limit) * 100 
   
    if percentage >= 100:
        status_of = "OVER-LIMIT"
    else:
        status_of = "OK"
    return difference, percentage, status_of

def print_report(credentials, value, limit, difference, percentage,status_of):
    """Prints out the information in the record"""
    print("=" * 34)
    print(f"RECORD CHECK - {credentials}")
    print("=" * 34)
    print("value:", value)
    print("limit:", limit)
    print("Difference:", difference)
    print("Percentage:", percentage, "%")
    print("status:", status_of)
    print("=" * 34)


records = [
    {
    "credentials": "srv-01",
    "value":  87.0,
    "limit": 120.0,
    }
]
for record in records:
    difference, percentage, status = check_record(record["value"], record["limit"])
    

print_report(record["credentials"], record["value"], record["limit"], difference, percentage, status)







#2
print()
def load_records(path):
    """Read label, value, limit from a file and return a list"""
    records = []
    with open(path) as e:
        for line in e:
            label, value, limit = line.strip().split(",")
            records.append({"credentials": label,        "value": float(value),        "limit": float(limit) })
    return records
records = load_records("eliana.rcds.txt") 
for e in records:
    print(e)           
   




#3
print()
def load_records(path):
    """Read label, value, limit from a file and return a list"""
    records = []
    with open(path) as e:
        for line in e:
            label, value, limit = line.strip().split(",")
            records.append({"credentials": label,        "value": float(value),        "limit": float(limit) })
    return records

try: 
     records = load_records("records_sample.txt")
except FileNotFoundError:
        print("This file is not found",) 
        records = []

count = 0 

for e in records:
    percentage = (e["value"] / e["limit"]) * 100
     
    if percentage >= 100:
            status = "OVER LIMIT"
    else:
            status = "OK"
    
    print(f"{e['label']}: {status}")
    print(f"OVER LIMIT: {count}")



  


