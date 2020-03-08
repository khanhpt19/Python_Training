celsius = input('Enter a number as temperature in Celsius: ')
while not celsius.isdigit():
    celsius = input('Temperature invalid, Enter again: ')
fahrenheit = (float(celsius) * 9/5) + 32
print('Temperature in Fahrenheit: ', fahrenheit)
