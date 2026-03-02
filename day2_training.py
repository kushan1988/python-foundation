given_data = ["math", "science", "math", "english", "science", "math"]
my_dict = {}
for x in given_data:
    if x in my_dict:
        my_dict[x] += 1
    else:
        my_dict[x]=1
print(f"Data: {my_dict}")
#Find most frequent
frequency_list = list(my_dict.values())
frequency_list.sort(reverse=True)
for x in my_dict:
    if my_dict[x] == frequency_list[0]:
        print(f"Most Frequent: {x}")
#optimized
max_count = 0
most_frequent = None
for x in my_dict:
    if my_dict[x] > max_count:
        max_count = my_dict[x]
        most_frequent = x

print("Most Frequent:", most_frequent)
#Practice 1
given_data = ["english","math", "science", "math", "science"]
my_dict = {}
for x in given_data:
    if x in my_dict:
        my_dict[x] += 1
    else:
        my_dict[x]=1
print(f"Data: {my_dict}")
#Most Frequent
max_count = 0
most_frequent = []
for x in my_dict:
    if my_dict[x] > max_count:
        max_count = my_dict[x]
for x in my_dict:
    if my_dict[x] == max_count:
        most_frequent.append(x)
print(most_frequent)
#optimized
max_count = 0
most_frequent = []

for key in my_dict:
    count = my_dict[key]

    if count > max_count:
        max_count = count
        most_frequent = [key]   # reset list

    elif count == max_count:
        most_frequent.append(key)

print(most_frequent)
#Practice 2
given_data = []
my_dict = {}
if not my_dict:
    print("No Data Available!")
else:
    for x in given_data:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x]=1
    print(f"Data: {my_dict}")
    #Most Frequent
    max_count = 0
    most_frequent = []
    for key in my_dict:
        count = my_dict[key]

        if count > max_count:
            max_count = count
            most_frequent = [key]   # reset list

        elif count == max_count:
            most_frequent.append(key)
    print(most_frequent)

    given_data = None

if not given_data:
    print("Empty")