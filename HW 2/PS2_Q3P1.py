'''The program returns a list of numbers from 1 to 1000 that contain 6'''

print("--------------------------------------------------------------")

lst = [i for i in range(1, 1001) if str(i).__contains__("6")]

print(lst)
