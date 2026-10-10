"""
RECORD CHECK  -  my version
===========================

Name  : Eliana Nakireru
Lane  : IT      (delete two)
Date  : 1st october, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

print("=" * 30)
label=(input("please write a label"))
print(f" RECORD CHECK - {label}")
print("=" * 30)
first = float(input("please write first value:"))
second= float(input("please write second value:"))
third = float(input ("please write third value:"))
print("=" * 30)
print("used :" , first)
print("total:" , second)
print("change" , third)



print()
print("=" * 34)
label=(input("please write a label"))
print(f" RECORD CHECK - {label}")
print("=" * 34)
first = float(input("please write first value:"))
second= float (input("please write second value:"))   
free = (second - first)
percent = (first/second) * 100
print("=" * 34)
print(f"used :  {first:>10.2f}")
print(f"total:  {second:>10.2f}")
print(f"free : {free:>10.2f}")
print(f"percent:{percent:>10.2f}" , "%")



# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
label=(input("please write a label"))
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
first = float(input("please write first value:"))
second= float (input("please write second value:"))   
difference = (second - first)
plus = (first + second)
percent = (first/second) * 100
print("=" * 34)
print(f"used :  {first:>10.2f}")
print(f"total:  {second:>10.2f}")
print(f"free : {difference:>+10.2f}")
print(f"Mine:  {plus:>10.2f}") #This helps clearly add the two values
print(f"percent:{percent:>10.2f}" , "%")

# : This helps clearly add the two values

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
