# # Python 101 course on Scrimba 2-21-2021
# print('Welcome to Python 101!')
# print("Create hammer")
# print("Use hammer")

# print("create nails")
# print("create hammer")
# print("use hammer and nails")

# a="it's"
# b='it\'s'

# failed_subjects=2.56
# name='John'
# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
# print(name + ' will need to redo ' + str(failed_subjects) + ' courses.')
# name="Eric"
# print(name + ' is doing well in geography.')

# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))

# a = int(1)          # a will be 1
# b = int(2.5)        # b will be 2
# c = int("3")        # c will be 3
# c1 = int(float("3.4"))   # c1 turns into a float first, will be 3
# d = float(1)        # d will be 1.0
# e = float(2.5)      # e will be 2.5
# f = float("3")      # f will be 3.0
# g = float("4.23")   # g will be 4.23
# h = str ("80s")     # h will be '80s'
# i = str(22)         # i will be '22'
# j = str(3.01)       # j will be '3.01'

# print([a,b,c,c1,d,e,f,g,h,i,j])

# print('Variables & Datatypes - Exercise')
# # Create appropriate Variables for Item name, the price
# # and how many you have in stock

# item_name = 'widget'
# price = 23.5
# inventory = 100
# is_in_inventory = True
# print(item_name, price, inventory)

# print("Basic Arithmetic")

# a=10
# b=3
# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)


# msg='welcome to Python 101: Strings'
# print(msg, msg)
# print(len(msg))
# print(msg.count('o'))
# # slicing
# print(msg[-3])
# print(msg[2:7])
# print(msg[:7])

# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
# print(msg1.title())
# print(msg1[::-1].title())

# msg="""Dear Terry,,
# You must cut down the mightiest
# tree in the forest with...
# a herring! <3"""
# print(msg)

# msg='Welcome to Python 101: Strings'
# print(msg.replace('Python',"C"))
# msg1=msg.replace('Python','C')
# print(msg)

# print('Python' not in msg)

# name='TERRY'
# color='RED'
# msg= '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# name= input('What is your name?: ')
# age=input('What is your age?: ')
# print('Hello ' + name + '! You are ' + age + ' years old.')

# num1=input('Enter a digit: ')
# num2=input('Enter a second number: ')
# answer=float(num1)+float(num2)
# print(answer)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')


# Lists:
# friends = ['John','Michael','Terry','Eric','Graham']
# #            0        1        2      3        4
# print(friends)
# print(friends[1],friends[4])
# print(friends[-1])
# print(friends[2:4])
# print(friends[:4])
# print(len(friends))
# print(friends.index('Eric'))
# print(friends.count('Eric'))

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# cars.sort()
# print(cars)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# friends.extend(cars)
# friends.insert('TerryG')

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# del friends[2]
# new_friends = list(friends)
# friends.pop(-1)
# friends.clear()
# print(friends)
# print(new_friends)

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter # of lemonades for new day: ')
# sales_w2.append(int(new_day))
# # sales.extend(sales_w1)
# # sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# # sales.sort()
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print('Welcome to Python 101: Split and Join')
# print(msg.split())
# print(msg.split(' '), type(msg.split(' ')))
# print(csv.split(','))
# print(''.join(friends_list))

# print(''.join(msg.split()))
# print(msg.replace(' ', ''))


# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
# friends_list = ['Exercise: fill me with names']
# print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

print((','.join(','.join(csv.split(';')).split(':'))).split(','))
friends_list = ['Exercise: fill me with names']
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

