import json
import numpy as np
from matplotlib import pyplot as plt

'''
input_file = open('getData.json', 'r')
output_file = open('getData.txt', 'w')
'''

f = open("outputDataNotSorted.txt", "r")

Lines = f.readlines()

mylist = []

count = 0
while(count < 1500):
    for line in Lines:
        data_int = float(line[:len(line)-2])
        mylist.append(data_int)
        count += 1

x = np.arange(0, len(mylist))
y = np.array(mylist)

plt.title("original data")
plt.xlabel("# of data")
plt.ylabel("time of data")
plt.plot(x, y, '.')
plt.show()

'''
print("length of list: ", len(mylist))

diff_list = []
for i in range(1, len(mylist), 1):
    diff = mylist[i]-mylist[i-1]
    diff_list.append(diff)

rounded_list = [round(num, 1) for num in diff_list]

# textfile = open("roundedDataNotSorted.txt", "w")
textfile = open("roundedData.txt", "w")
for element in rounded_list:
    textfile.write(str(element) + "\n")
textfile.close()

x = np.arange(0, len(rounded_list))
y = np.array(rounded_list)

plt.title("diff_sorted")
plt.xlabel("order")
plt.ylabel("time difference")
plt.plot(x, y, color="green")
plt.ylim(-10000, 20000)
plt.xlim(0,len(rounded_list))
plt.show()
'''
