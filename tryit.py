import rsaidnumber
from datetime import datetime

id_number = rsaidnumber.parse('7710135929187')

print(id_number.date_of_birth)

mylist = [12,2,3,4,11]
mylist1 = [11,9,6,8,12]
newlist = []

mylist.sort()
mylist1.sort()
for x in mylist:
    if x in mylist1:
        newlist.append(x)
print(len(newlist))