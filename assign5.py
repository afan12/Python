def find_longest_word(): #find the longest word function
    text = input("Enter a few words and I will find the longest: ") #asking the user to input the words
    longest = 0    
    for word in text.split(): #evaluating length of each word
        if len(word) > longest:
            longest = len(word)
            longest_word = word
    print( "The longest word is: %s" % longest_word ) #the word with the longest length is
find_longest_word()

p = [] #positive numbers
n = [] #negative numbers
a = [] #all numbers

print("Please enter some positive, negative or zero numbers to determine the average: ")
values = []
for i in iter(lambda: int(input("Enter a number (-9999 to end): ")), -9999):
    if i >= 0: 
        p.append(i)
    else: 
        n.append(i)
    a.append(i) 

def posNumAvg(values):
    return sum(values) /len(values)

def nonPosAvg(values):
    return sum(values) / len(values)

def allNumAvg(values):
    return sum(values) / len(values)

dictionary = {
    "AvgPositive": posNumAvg(p),
    "AvgNonPos": nonPosAvg(n),
    "AvgAllNum": allNumAvg(a)
}

print("The dictionary with averages is:")
print(dictionary) 
