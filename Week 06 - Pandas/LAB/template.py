"""
RECORD CHECK  -  my version
===========================

Name  : Eliana Nakireru
Lane  :  AI / Cyber / IT      (delete two)
Date  : 30th October, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# 1. Threshold
import pandas as pd

"""Read record from created CSV file and calculate the percentage and print dataframe."""

sample = pd.read_csv("eliana_records.csv")

sample["percent"] = (sample["used_gb"]/sample["total_gb"]) * 100

print(sample)







#2. Typical
import pandas as pd

sample = pd.read_csv("eliana_records.csv")

sample["percent"] = (sample["used_gb"]/sample["total_gb"]) * 100

"""Add a status to each record and display only the ones that are not OK."""

sample["status"] = sample["percent"].apply(
    lambda s : "OVER LIMIT" if s >= 100 else "WARNING" if s >= 90 else "OK"
)
filter = sample[sample["status"]!="OK"]
print()
print(filter)







#3. Excellent
import pandas as pd
import matplotlib.pyplot as plt

sample = pd.read_csv("eliana_records.csv")

sample["percent"] = (sample["used_gb"]/sample["total_gb"]) * 100

sample["status"] = sample["percent"].apply(
    lambda s : "OVER LIMIT" if s >= 100 else "WARNING" if s >= 90 else "OK"
)
filtered = sample[sample["status"]!="OK"]
print()
print(filtered)

"""Group records by status and count each per group, save to a new CSV file and create a bar chart of counts per status."""

count_per_group = sample.groupby("status")
print(count_per_group.size())

sample.to_csv("nakireru_new.csv", index=False)

count_per_group.size().plot(kind="bar", title= "No. of counts per status")
plt.ylabel("No. of servers")
plt.tight_layout()
plt.savefig("counts_per_status.png")
plt.show()




