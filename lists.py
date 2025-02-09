"""
Lists Execises
Alex Spicher
"""
print('list basics')
animals = ['dog', 'cat', 'bird', 'cow'] #lists uses square brackets, we can assign a list to a variable
print(animals) #displays full list
print(animals[0]) #this will print the first value in animals list (python starts at 0)
print(animals[3]) #this will print the fourth value
print(len(animals)) #len can be used to return the length of any given variable
#in this instance, len is used to return the length of the list, which is 4
print('------------------------------')

print('FOR and IN commands')
numbers = [2, 4, 6, 8] #this list is filled with integers, so we can perform mathematical actions
sum = 0 #set the sum variable equal to zero
for num in numbers: #applies the next line to each variable in our list
    sum += num #this will loop through the list and add each number to zero (we set sum to zero)
print(numbers) #displays full list
print(sum) #this will display the new sum variable after adding each number in our list
print('------------------------------')

print('adding and removing list items')
example = ['Bob', 'Mike', 'Joe', 'Chris'] #create a list of names
print(example) #display the full list
example.append('Jerry') #append will add a new item to our list, in this case the name Jerry
print(example)
example.remove('Chris') #this will remove an item, in this case the name Chris
print(example)