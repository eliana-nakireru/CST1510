"""
RECORD CHECK  -  my version
===========================

Name  :Eliana Nakireru
Lane  :  AI / Cyber / IT      (delete two)
Date  :10th oct, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
#1(Threshold)
print("=" * 34 )
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
print("=" * 34 )
label = (input("please enter a label"))
print(f"RECORD CHECK - {label}")
print("=" * 34 )
value = float(input("please enter a value:"))
limit = float(input("please enter a limit:"))

difference = value - limit
print("Difference:", difference)
percent = (value / limit) * 100
print("Percent:" , percent )

status_of(percent)
print("status:", status_of(percent))
print ("=" * 34)






#2(Typical)
print()
def check(value, limit):
    
    difference = value - limit
    print(f"difference: {difference:>10.2f}")
    percentage = (value/ limit) * 100
    
    print(f"percentage: {percentage:>10.2f}")
    return difference, percentage

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
value = float(input("please enter a value:"))
print(f"value: {value:>10.2f}")

limit = float(input("please enter a limit:"))
print(f"limit: {limit:>10.2f}")

feedback = (check(value, limit))
print(feedback)

difference, percent =check(value, limit)







#3(Excellent)
print()
def print_report(label, value, limit, difference, percent, status):
    print("=" * 34 )
label = (input("please enter a label"))
print(f"RECORD CHECK - {label}")
value = (input("please enter a value"))
print(f"Value:, {value}")
limit = (input("please enter a limit"))
print(f"limit:, {limit}")
print(difference)
print(percent)
print(status_of)
print("=" * 34)

def check(value, limit):
    difference = value - limit
    percentage = (value/ limit) * 100

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"












