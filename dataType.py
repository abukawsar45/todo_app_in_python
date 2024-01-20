# data type

num = 10
for i in range(num):
  print (i + i)

# index is first argument in range
num2 = 10
for i in range(num2-4, num2):
  print (i)

# reverse way in range
'''last value (-2) is every time minus and then true then execute next part in loop'''

# ren=range(9)
# print(ren) // range(0,9)

num3 = 10


for i in range(num3, 0, -2):
  print (i)

# multiplication with loop
num4 = 10
for i in range(1, num4+1):
  result = i * 3
  print (f'3 x {i} = {result}\n')


# while loop
num5 = 0

# while True:
#   if num5 == 49:
#       break
#   print(f'This is no. {num5} index')
#   num5 += 7

# while num5 <= 49:
#   print(f'This is no. {num5} index')
#   num5 += 7


# collection
''' list/ tuple/ dictionary / set '''
  # list

fruitList = ['mango', 'pineapple', 234, 34.342j]
# getSpecificFood = fruitList[-1]
# getSpecificFood = fruitList[-3]
# getSpecificFood = fruitList[:4]
getSpecificFood = fruitList[3:4]

print(getSpecificFood)


# condition 
'''list = array = [] = mutable // toupe = () = immutable // set = object = {} == mutable // sort '''

fruits = ['mango', 'banana', 'pineapple', 'potato']

for fruit in fruits:
  print(fruit)

fruits[3] = 'Lady finger'

# check system
target = 'Banana'

# print('banaan' in fruits)
print(target in fruits)

'''last level add'''
addFruit = 'watermelon'
fruits.append(addFruit) 
print(fruits)

'''index base add'''
addFruit2 = 'others'
fruits.insert(0, addFruit2)
print(fruits)



''' remove // pop '''
# fruits.remove(addFruit)
# fruits.remove(fruits[1])
print(fruits)

fruits.pop(0)
print(fruits)

# fruits.clear()
print(fruits)

# sort

# fruits.sort()
fruits.sort(reverse = True)
print(fruits)

ab = True
cd = None
print(cd)

'''immutable // not append or remove   '''
fruits_Tup = ('Abu Kaw Sar', 'Rasel', 'Abu Kaw Sar', 'Mostofa' )
getData = fruits_Tup[1]

print(fruits_Tup, getData)

for item in fruits_Tup:
  print(item)

update_tup = list(fruits_Tup)
print(update_tup)

update_tup.append('Ershad')
print(update_tup)

print(update_tup[3])

fruits_Tup = tuple(update_tup)
print (fruits_Tup)


# set-------------SET--------------------- not allow duplicate value // random index
fruits_set = { 'ami', 'you', 'we', 'ami', 'us', 'they'}
fruits_set2 = {'he', 'she', 'ami', 'us', 'they'}
print(fruits_set)

# fruits_set=fruits_set2
fruits_set2.update(fruits_set)
# fruits_set.update(fruits_set2)
# fruits_set2.union(fruits_set)
print(fruits_set2)
print(fruits_set)

# fruits_set.([2])
for setItem in fruits_set:
  print(setItem)

update_set = list(fruits_set)
print(update_set)

update_set.append("ammu")
print(update_set)

update_set.remove('us')
print(update_set)

print(update_set[1])

fruits_set = set(update_set)
print(fruits_set)

# dictionary
profile = {
  "name" : "kawsar",
  "skill" : "HTML, CSS, JavaScript, React",
  "experience" : "1 year"
}

print(profile)
print(profile['skill'])
print(profile.keys())
print(profile.values())

profile['experience'] = "2 years"
print(profile)
# add
profile['proffesion'] = "web developer"
print(profile)

for info in profile.keys():
  print(info)
  
for info in profile.values():
  print(info)
