# The main purpos of this project is teach you how to concatinating strings

## String can be concatenated in the following form

name='Getachew'

print("My name is "+name)
print("My name is {}".format(name))
print(f"My name is {name}") # Mosty used form

# Madlibs: What I am going to do is enter adjactive or verp or Noun and It will constract somthing constracted in the form of pharagrhs
programming_language=input("Programming Language:")
trend_tech = input("Tranding technology:")
trend_tech2 = input("Tranding technology:")
madlibs= f"{programming_language} is an interesting programming language and It can be use for web development, {trend_tech} and {trend_tech2}"
print(madlibs)