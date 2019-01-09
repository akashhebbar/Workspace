words = {"woof":A,"arf bark":B}
input = "woof,arf bark"
inputList = input.split(',')
for word in inputList:
    print words[word]