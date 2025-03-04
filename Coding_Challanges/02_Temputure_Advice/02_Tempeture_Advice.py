#Making a Code for temputure it will also be in celcius
#Made By Bilal Shamsi
temperature = float(input("Enter the temperature: "))
if temperature < 10:
    print("It's cold outside. Wear a jacket or a full sleeve!")
elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool and hydrated!")
