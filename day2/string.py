# author: zzq

name = "my \tname is {name} and i am {year} old."

print(name.capitalize())
print(name.count("a"))
print(name.center(50, "-"))
print(name.endswith("ex"))
print(name.expandtabs(tabsize=30))
print(name[name.find("y"):])
print(name.format(name='alex', year=23))
print(name.format_map({'name':'alex', 'year': 12}))
print('name123'.isalnum())
print('abA'.isalpha())
print('1A'.isdecimal())
print('1A'.isdigit())
print('aA'.isidentifier())  # 判断是不是一个合法的标识符
print('aA'.islower())
print('33.33'.isnumeric())
print(' '.isspace())
print('My Name Is '.istitle())
print('My Name Is '.isprintable())  # tty file, drive file
print('My Name Is '.isupper())
print('+'.join(['1', '2', '3', '4']))
print(name.ljust(50, '*'))
print(name.rjust(50, '-'))
print('Alex'.lower())
print('Alex'.upper())
print('\nAlex'.lstrip())
print('\nAlex\n'.rstrip())
print('    Alex\n'.strip())


p = str.maketrans("abcdef", '123456')

print("alex li".translate(p))

print('alex li'.replace('l', 'L', 1))
print('alex lil'.rfind('l'))
print('1+2+3+4'.split('+'))
print('1+2\n+3+4'.splitlines())
print('Alex Li'.swapcase())
print('Alex Li'.title())
print('Alex Li'.zfill(50))

print('---')


