x=input("1st Colour:")
y=input("2nd Colour:")
z=input("3rd Colour:")
w=input("4th Colour:")

first_value = {"black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "gray": 8,
    "white": 9,
    "gold":10,
    "silver":11
  }
second_value = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "gray": 8,
    "white": 9,
    "gold":10,
    "silver":11
}
third_value = {
    "black": 10**0,
    "brown": 10**1,
    "red": 10**2,
    "orange": 10**3,
    "yellow": 10**4,
    "green": 10**5,
    "blue": 10**6,
    "violet": 10**7,
    "gray": 10**8,
    "white": 10**9,
    "gold": 10**-1,
    "silver": 10**-2
}
fourth_value = {
    "black": "+/-1%",
    "brown": "+/-2%",
    "green": "+/-0.5%",
    "blue": "+/-0.25%",
    "violet": "+/-0.1%",
    "gray": "+/-0.05%",
    "gold": "+/-5%",
    "silver": "+/-10",
    "red": "",
    "orange": "",
    "yellow": "",
    "white": ""

}
print( str(first_value[x]) + str(second_value[y]) +"*"+ str(third_value[z]) + str(fourth_value[w]))

