def Math(divide7):
  try:
    divide = float(divide7)/7
    # print (divide)
  except:
    divide = 'You cant calculate strings.'
  return divide

with open("file.txt","r") as openFile:
  for placeholder in range(10):
    fileContents = openFile.readline()
    print(Math(fileContents))


# openFile = open('file.txt','r')
# fileContents = openFile.readline()
# openFile.close()


