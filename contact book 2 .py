names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input('Name: ')
    phone_number = ('Phone Number: ')
    names.append(name)
    phone_number.append(phone_number)

print('\nName\t\t\tPhone Number\n')

for i in range(num):
    print('{}\t\t\t{}'.format(names[i], phone_numbers[i]))

search_term = input('\nEnter Search Term:')
print('Search Result')
if search_term in names:
    index = names.index(search_term)
    phone_number - phone_numbers[index]
    print('Name {}, Phone Number: {}'.format(search_term, phone_number))
else:
    print('Name not found')
