import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import numpy

countries = [30, 31, 32, 33, 34]  # To call out the whole countries of non asia non europe which has 5 columns
row = [2]  # Start reading the excel file from row 2
df = pd.read_excel('IMVA.xlsx', sheet_name='IMVA', usecols=countries)  # to read the excel file

pd.set_option('display.max_columns', 30)  # to preview the whole 5 columns, if delete there will be semi colons
pd.set_option('display.max_rows', 122)  # to preview the whole of 122 rows, if delete it wont preview the whole 2 rows
ranges = (df.iloc[2:122, :34])  # the start printing from rows 2 to 122 and from 30 to 34

calculated = (df.iloc[2:122, :34].sum(axis=0))  # Sum of whole value from 2-122 & from 30-34
top3 = (df.iloc[2:122, :34].sum(axis=0).nlargest(3))  # Print out top 3 largest value country using n.largest



print(ranges)
print(calculated)
print(top3)

graph = calculated[[' Australia ', ' USA ', ' New Zealand ']].plot(kind='bar', title="Top 3 Country In Non-Asia and Non-Europe", figsize=(10,10), legend=True, fontsize=12)


plt.show()

my_fig = graph.get_figure()
my_fig.savefig("TopCountries.png")