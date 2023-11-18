print(" °C   °F")




for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:3}   {fahrenheit:3}")

