# Ex05.2 write some variables that convert the inches and pounds to centimeters and kilograms.
while True:
    amount, unit = raw_input('Enter amount with units separated by spaces and units in [cm,in,kg,pound]: ').split(' ')
    converted_data = float(amount) * {'in': 2.54, 'cm': 0.393701, 'pound':0.453592, 'kg': 2.20462}[unit]
    print(str(converted_data) + {'in': 'cm', 'cm': 'in', 'pound': 'kg', 'kg': 'pound'}[unit])
