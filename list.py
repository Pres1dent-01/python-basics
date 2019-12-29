#List are mutable
#to create a list
courses = ['history','maths', 'biology', 'comp_sci' ]
print(courses)

# to find total values in list
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:3])

#to add anything in list 
courses.append('Art')
print(courses)
#to add anything in specific location 
courses.insert(0,'Art')
print(courses)

'''#to add two list
courses2 = ['Art', 'Education']
courses.insert(0, courses2)
print(courses)
print(courses[0])

#to add to list 
courses.extend(courses2)
print(courses)

#to remove any value in list
courses.remove('biology')
print(courses)

pooped = courses.pop()
print(pooped)               #mostly used in stack
print(courses)'''

'''#to reverse
courses.reverse()
print(courses)
'''
#sort sorts the list in alphabetical order
courses.sort()
print(courses)
nums = [1, 4, 3, 5, 2]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#to sort without disturbing the original
sorted_courses = sorted(courses)
print(sorted_courses)

#to find min max and sum
print(min(nums))
print(max(nums))
print(sum(nums))

#to find index of a value
print(courses.index('history'))

#to check value in list
print('Art' in courses)

for item in courses:
    print(item)

#to introduce the courses with index use enumerate
for index, item in enumerate(courses):
    print(index, item)

#to start the index value from 1
for index, item in enumerate(courses, start = 1):
    print(index, item)

#join function in python
courses_str = '--'.join(courses)
print(courses_str)
new_list = courses_str.split('--')
print(new_list)
