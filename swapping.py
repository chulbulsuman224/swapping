def swappFileData():
    filename=input("Enter the file")
    numberofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)

swappFileData()