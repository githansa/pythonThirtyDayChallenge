print('Hello Day Four')

my_list = [1, 5, 7]
for my_var in my_list:
    print(my_var)

for i in "ABC":
    print(i)

    # for x in 10:
    # print(x)
    # #TypeError: 'int' object is not iterable

for x in range(0, 5):
    print(x)
# homework define 2 users with username and ID
# assign the users to a dictionary called my_users
# Print Values using a for loop

user_one = {"Name": "Gian",
            "Address": "1235 Olathe",
            "Info": "Cls",
            "email": "gihan@gmail.com"}

user_two = {"Name": "Joe",
            "Address": "1235 KC",
            "Info": "Prius",
            "email": "gihan@gmail.com"}

my_users = [user_one, user_two]

for users in my_users:
    print(users)
   #print(users['Info'])

for users in my_users:
    if 'email' in users:
        print(users['email'])
