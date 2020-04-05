# Import declarations go here
import pandas
import random
import xlrd

# Title: realloc.py
# Authors: Harsha Cheemakurthy, Anna Robbins
# Hack the Crisis Sweden 2020

# test variable declaration; will be changed later to follow a statistical model

wb1 = xlrd.open_workbook("C:/users/arobb/PycharmProjects/untitled/Sample_unemployment_Stockholm_30.xlsx")
sheet1 = wb1.sheet_by_index(0)

wb2 = xlrd.open_workbook("C:/users/arobb/PycharmProjects/untitled/Sample_job_openings_Stockholm.xlsx")
sheet2 = wb2.sheet_by_index(0)


unemployed = random.randrange(300000,
                              1000000)  # This is a number representing people who are currently unemployed.
employed: int = 0  # This is the number of workers who will be reallocated to new or temporary jobs.
reserve: int = 0  # This is the number of workers who will not be reallocated to new or temporary jobs due to risk factor or lack of demand.
# TODO
jobopenings = random.randrange(100000,
                               900000)  # This is a random number between 100k-900, representing available job openings.
stillopen = random.randrange(0,200000)
employmentrate = (jobopenings-stillopen)/unemployed # This represents the percentage (between 0 and 1) expected reemployment; will be randomly generated later.
# Note that it is not realistic to have 0 job openings in the end, i.e., not all available positions will be filled.
# This has been modelled by subtracting a randomly generated number between 0-200k from job openings.

employed = jobopenings-stillopen
reserve = unemployed * (1 - employmentrate)

print(
    'Base unemployed: ', unemployed, '\n Reemployed: ', employed, '\n Reserve: ', reserve, '\n Employment rate: ', employmentrate)

# TODO
# Maybe we should separate unemployed people by sector/profession and try to reallocate based on skillsets as pitched.