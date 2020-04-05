# Import declarations go here
import pandas
import random
import xlrd

# Title: realloc.py
# Authors: Harsha Cheemakurthy, Anna Robbins
# Hack the Crisis Sweden 2020

# open spreadsheets to extract data
pd1 = pandas.read_excel('Sample_unemployment_Stockholm_30.xlsx')
pd2 = pandas.read_excel('Sample_job_openings_Stockholm.xlsx')

# TEST
# print(pd1)
# print(pd2)

# UNEMPLOYMENT
unemployed = pd1.iloc[0:7, 2]
reserve = []                # number that remains unemployed after reallocation, due to health risk or skill mismatch
length = len(unemployed)
i = 0

# Assume that 70-90% of each occupation in the currently unemployed workforce with a desirable skillset can be
# reemployed immediately in a current opening.
# For occupations without desirable skillsets, assume that 30-50% can be reemployed immediately in a current opening.
for i in range(0,length):
    if i!=3 and i!=4:
        reserve.append(int(unemployed[i]*(100 - random.randrange(70, 90))/100))
    else:
        reserve.append(int(unemployed[i]*(100 - random.randrange(30,50))/100))
# TEST
# print(reserve)

# TOTAL EMPLOYMENT
employed = pd1.iloc[0:7, 1]  # total employed after reallocation, incl. original employment and reallocated employment
reallocate = []              # number in each occupation A-F and Other to be reallocated to jobs W-Z
i = 0
for i in range(0,length):
    temp = unemployed[i] - reserve[i]
    reallocate.append(temp)
    employed[i] = int(employed[i] + temp)
# TEST
# print(employed)
# print(reallocate)

# REALLOCATION
    # Assume skillsets overlap between occupations:
    # A and W;
    # B, C and X;
    # F and Y, Z
job_openings = pd2.iloc[0:4,1]
reallocated_results = job_openings      # number of workers in occupations W-Z after reallocation
length2 = len(job_openings)

reallocated_results[0] = reallocated_results[0] + reallocate[0]                     # add reallocated employees from A to W
reallocated_results[1] = reallocated_results[1] + reallocate[1] + reallocate[2]     # add reallocated employees from B,C to X

split_yz = random.randrange(0,100)          # random percentage to determine how occupation F is split between Y and Z
realloc_y = reallocate[5]*split_yz/100
realloc_z = reallocate[5]*(100-split_yz)/100

reallocated_results[2] = reallocated_results[2] + realloc_y
reallocated_results[3] = reallocated_results[2] + realloc_z

# TEST
print(reallocated_results)
