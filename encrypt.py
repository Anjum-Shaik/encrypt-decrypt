inputtext = input()
key = 4
mode  = "decrypt"
ledger = "abcdefghijklmnopqrstuvwxyz 1234567890"
outputtext = " "
for char in inputtext:
    inputindex = ledger.find(char)
    if mode == "encrypt":
       outputindex = inputindex + key
    elif mode == "decrypt":
       outputindex = inputindex - key
    if outputindex >= len(ledger):
       outputindex = outputindex - len(ledger)
    elif outputindex < 0:
       outputindex = outputindex + len(ledger)
    outputtext = outputtext + ledger[outputindex]
print(outputtext)
