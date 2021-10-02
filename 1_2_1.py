name='Iryna'
day='Tuesday'
#1
print('Good day, '+ name +'! '+ day + ' is a perfect day to learn some python')
#2
print('Good day, %s! %s is a perfect day to learn some python' %(name, day))
#3
print (f'Good day, {name}! {day} is a perfect day to learn some python')
#4
print('Good day, {}! {} is a perfect day to learn some python'.format(name, day))
#5
print('Good day, {1}. {0} is a perfect day to learn some python'.format(day, name))
