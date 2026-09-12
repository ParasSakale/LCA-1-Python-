#Python program to create, append and remove etc.
# operation on Dictionary and Tuple.

#Dictionary

my_dict = {
    "name": "Cristiano",
    "age": 41,
    "car": "Ferrari"
}
print(my_dict)

my_dict["city"] = "Madeira"
print(my_dict) #Adding another key-value pair to the dictionary.

my_dict["car"] = "Bugatti"
print(my_dict) #Changing the value of the key "car".

x = my_dict.values()
print(x) #Prints all the values of the dictionary as a dict_values view object

y = my_dict.keys()
print(y) #Prints all the keys of the dictionary as a dict_keys view object

my_dict.pop("car")
print(my_dict) #Removing the key-value pare "car": "ferrari"


my_dict = {
    "name": "Cristiano",
    "age": 41,
    "car": "Ferrari"
}
print(my_dict)

del my_dict["car"]
print(my_dict) #2nd method for deleting the key-value pair.


#Tuples

my_tuple = (1,2,3,4,5)

# As tuples are immutable, we cannot add a vlue in it by the .append() method.
# so let's convert the tuple into a list (temporary list).

temp_list = list(my_tuple)
temp_list.append(6)
my_tuple = tuple(temp_list)#converting the temporary list back to tuple

print(my_tuple)

my_tuple_2 = (1,2,3,4,5,6,7)
# As tuples are immutable, we cannot delete a vlue in it by the del method.
# so let's convert the tuple into a list (temporary list).

temp_list_2 = list(my_tuple_2)
del temp_list_2[5]
my_tuple_2 = tuple(temp_list_2)#converting the temporary list back to tuple

print(my_tuple_2)


#List

my_list = [0.45, 7, "Rohit"]
print(my_list)

my_list.append(45)
print(my_list)# Adding a new value to the end of the list

my_list.insert(1, "Cristiano")
print(my_list)# Adding a new value at a certain index to the list

my_list.remove(0.45)
print(my_list)#Removing an item from teh list

my_list_1 = [0.5,"Cristiano", 7, "Rohit", 45]
print(my_list_1)
x = my_list_1.pop(0)#another method for removing an item from the list
print(my_list_1)#but .pop() if assigned to a different variable also stores it
print(x)#the item popped is stored in x

my_list_2 = [0.5,"Cristiano", 7, "Rohit", 45]
print(my_list_2)
del my_list_2[0]
print(my_list_2)#another method for removing an item from the list

new_list = ["watermelon", "mango", "banana", "apple", "pineapple"]
y = new_list[2]
print(y)#This helps to read a value at a specific index

new_list[4] = "orange"
print(new_list)#changing the value at a specific index

print(len(new_list)) #Tells how many values are there in a list

new_list_2 = [75, 474, 34, 343, 3478]
print(new_list_2)#prints the list
new_list_2.reverse()
print(new_list_2)#Reverses the complete list

new_list_3 = [22,45,3,7,746,12,33,56,67]
print(new_list_3)#prints the list
new_list_3.sort()
print(new_list_3)#Arranges the list in an ordered form from low to high
new_list_3.reverse()
print(new_list_3)#Reverses the arranged list

list_1 = [10,20,30,40,50]
print(list_1)
list_1.extend([100,200,300,400,500])
print(list_1)

print(20 in list_1)#prints True
print(80 in list_1)#prints False

#The difference between .extend() and .append() is that
# .extend() adds the new values normally, but the
# .append() adds new values in form of nested list

list_2 = [11,22,33,44,55]
list_2.append([66,77,88,99])
print(list_2)

list_3 = [33,44,55]
list_3.extend([66,77,88,99])
print(list_3)