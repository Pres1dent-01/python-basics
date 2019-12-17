message = "Hello world"
messag =  'Hello\'s world'
mess = "hahahahahaahha"
print(messag)
print(message)
#to write multiline string use """" 
hi = """This is a multiline string
i can write as many lines as i need"""
print(hi)
print(len(hi))
print(message[4])
print(len(messag))
print(messag[5])
print(messag[12])
print(message[0:5])
print(messag[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(mess.count('ha'))
print(message.count("Hello"))
print(message.find("world")) #If the word dosent exist it will give output as -1
message = message.replace("world","Universe") #It is case sensitive
print(message)
greeting = "Hello"
him = "Bob Marley"
musician = greeting + " " + him
print(musician)

#string formatting
chinmay = "yooo"
vagish = "mannnnnn"
hijball = "{} {} welcome".format(chinmay, vagish)
print(hijball)

#string formatting only for version higher than 3.6 is supported :-)
mayur = "yoyoyo"
sojitra = "mamamamam"
rat = f"{mayur} {sojitra.upper()} Welcome"
print(rat)

#kundli nikalne k liye ki kaunsa kaunsa methods class wagera use kia hai humne is variable k liye
print(dir(mayur))
#print(help(str))
#print(help(str.lower))