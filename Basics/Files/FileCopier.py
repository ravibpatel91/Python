sourceInput = input("Enter Source File Name : ")
source = open(sourceInput, "r")
destInput = input("Enter Destination File Name : ")
destination = open(destInput, "w")
destination.write(source.read())
print("File Successfully Copied : " + destInput)
source.close()
destination.close()
destination = open(destInput, "r")
print("File " + destInput + " Contents : " + destination.read())
destination.close()
