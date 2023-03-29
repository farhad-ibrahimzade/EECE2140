'''The program returns the common elements of two user-entered sets'''

# TODO: The program the code recognizes a duplicate element in one list as a common element
#  even though the other list doesn't have the element

print("--------------------------------------------------------------")

firstList = {int(num) for num in
             input("Please enter the first list: ").split()}

secondList = {int(num) for num in
              input("Please enter the second list: ").split()}

combined = list[firstList] + list[secondList]

length = len(combined)

# Remove non-common elements
for i in combined:
    if combined.count(i) == 1:
        combined.remove(i)

print("Common elements: ")

# Use a set to make common elements appear once
for num in set(combined):
    print(num, end=" ")
