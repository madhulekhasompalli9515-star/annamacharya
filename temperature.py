num=float(input("enter temp:"))
choice=input("enter c for celcius and f for fahrenheit:")
if choice=="c":
    f=num*(9/5)+32
    print(f"fahrenheit:{f}")
elif choice=="f":
    c=(num-32)*5/9
    print(f"celcius:{c}")
else:
    print("invalid choice")


'''
OUTPUT:
==== RESTART: C:/python/temperature.py ====
enter temp:28.7
enter c for celcius and f for fahrenheit:c
fahrenheit:83.66

==== RESTART: C:/python/temperature.py ====
enter temp:83.66
enter c for celcius and f for fahrenheit:f
celcius:28.699999999999996
'''
