"""
RECORD CHECK  -  my version
===========================

Name  : Eliana Nakireru
Lane  :  IT    
Date  : 23rd October, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# 1. (THRESHOLD)
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit 

a1 = Record("srv-01", 87.0, 120.0)
a2 = Record("srv-02", 50.0, 100.0)

print("=" * 34)
print("Label:",  a1.label)
print("Value:",  a1.value)
print("Limit:",  a1.limit)
print("=" * 34)

print("=" * 34)
print("Label:", a2.label)
print("Value:",  a2.value)
print("Limit:",  a2.limit)
print("=" * 34)






# 2. (TYPICAL)
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING Or OK based on percent of value and limit"""
        p = (self.value / self.limit) * 100
       
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

a1 = Record("srv-01", 87.0, 120.0)
a2 = Record("srv-02", 150.0, 100.0)

print()
print()
print("=" * 34)
print("Label:", a1.label)
print("Value:", a1.value)
print("Limit:", a1.limit)
print("Status:", a1.status())
print("=" * 34)

print("=" * 34)
print("Label:", a2.label)
print("Value:", a2.value )
print("Limit:", a2.limit)
print("Status:", a2.status())
print("=" * 34)







# 3. (EXCELLENT)
class Record:
        

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT Or OK based on percent of value and limit"""
        p = (self.value / self.limit) * 100
         
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
             return "WARNING"
        else:
            return "OK"

def load_records(path):
    """Read record from a file and return a list of Records"""
    records = []
    with open(path) as e:
        for line in e:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

over_limit_count = 0

records = load_records("eliana.rcds.txt")

for record in records:
    print()
    print("=" * 34)
    print("Label:", record.label)
    print("Value:", record.value)
    print("Limit:", record.limit)

    status = record.status()
    print("Status:", record.status())

    if status == "OVER LIMIT":
        over_limit_count += 1
    
    print("=" * 34)

print("No. of OVER LIMIT:", over_limit_count)



       

