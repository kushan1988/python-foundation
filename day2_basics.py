#Remove Duplicates
#Using List
given_list = [1,2,2,3,4,4,5]
my_list = []
for x in given_list:
    if x not in my_list:
        my_list.append(x)
    else:
        print("Duplicate Found!")
my_list.sort()
print(my_list)
#Using Sets
given_set = {1,2,2,3,4,4,5}
print(given_set)
#Find Second Largest
#Using List
given_list = [10,20,20,5]
given_list.sort()
my_list = []
for x in given_list:
    if x not in my_list:
        my_list.append(x)
    else:
        print(f"Duplicates:{x}")
print(my_list[-2])
#Reverse List
given_list = [1,2,3,4,5]
my_list = []
i = len(given_list)-1
print(i)
while i >= 0:
    my_list.append(given_list[i])
    i=i-1
print(my_list)
#Frequency Counter
given_list = [1,2,2,3,3,3,4]
my_list = []
my_dict = {}
for x in given_list:
    if x not in my_list:
        my_list.append(x)
    else:
        print(f"duplicates!")
for x in my_list:
    count = 0
    for y in given_list:
        if x == y:
            count= count +1
            print(x,count)
    my_dict[x]=count
print(my_dict)
#Frequency Counter (Improved Code)
given_list = [1,2,2,3,3,3,4]
my_dict = {}
for x in given_list:
    if x in my_dict:
        my_dict[x] += 1
    else:
        my_dict[x] = 1
print(my_dict)