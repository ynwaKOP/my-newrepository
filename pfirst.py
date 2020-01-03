adress = ["19","compus dr","slc"]
pins = {"tom":123,"bob":456,"mike":789}

#print(adress)

usr = input("enter your name: ")
#pin  = int(input("Enter your pin: "))

if usr in pins.keys():
	pin = int(input('Enter your pin '+usr+": "))
	if pin == pins[usr]:
        	print("Welcom! "+usr+'!' )
	else:
       		 print("no privilege")

else:
	print("No such user!")


