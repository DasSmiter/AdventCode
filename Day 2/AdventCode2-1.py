import math

with open('AC2Input.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

#1. Parse the input into an array, 1 field per ID pair
#2. All pairs are min-max format.  Extract the min and max into minArray and maxArray.  mArrays should be the same size
#3. Create an array idArray of all values (ids) between min and max, inclusive
#4. Check the idArray from start to finish for repeating values.  Values can be a single character, or a phrase.  The array is a hit (repeat) only if
#4a. the entire value is made up of a chunk that repeats exactly.  For example, 1212 is a hit because '12' repeats twice to make the whole value.  1231 is not a hit because no chunk repeats to make the whole value
#4a. So we will need to split up the word into a half-word chunk, then check that chunk against the whole.
#5. Output the sum of all repeating values found in step 4

#define our functions up front because python

def findChars(line, character): #this function finds all instances of 'character' in 'line' and returns an array of their positions
    characters = [] #this should be an array of positions for the character we're searching for
    for j in range(len(line)):
         if(line[j] == character):
            characters.append(j)
    return characters

#1.  Parse the input into an array, 1 field per ID pair
line = content[0].strip()
rangeDelimiters = findChars(line, ',')

parsedInput = []

for i in range(len(rangeDelimiters)):
    if i == 0:
        parsedInput.append( line[0:rangeDelimiters[i]] )  #input from 0->last character before the delimiter
    elif i == len(rangeDelimiters)-1:
        parsedInput.append( line[rangeDelimiters[i-1]+1:rangeDelimiters[i]] ) #input from the previous delimiter to just before this one
        parsedInput.append( line[rangeDelimiters[i]+1:len(line)] ) #input from the last delimiter to the end of the line to capture the last line
    else:
        parsedInput.append( line[rangeDelimiters[i-1]+1:rangeDelimiters[i]] ) #input from the previous delimiter to just before this one
print('Parsed Input: ', parsedInput)
#/1

#2. All pairs are min-max format.  Extract the min and max into minArray and maxArray.  mArrays should be the same size
minmaxDelimiters = [[-1, -1] for _ in range(len(parsedInput))]  #this will be a 2D array, each entry will be an array of the positions of the '-' characters in each min-max pair.  However this is just the initialzied array
for i in range(len(parsedInput)):
    minmaxDelimiters[i] = [i, findChars(parsedInput[i], '-')[0]] #this should assign the array of '-' positions to the correct entry in the 2D array


minArray = []
for i in range(len(minmaxDelimiters)):
        minArray.append( int(parsedInput[i][0:minmaxDelimiters[i][1]]) )  #input from 0->last character before the delimiter


maxArray = []
for i in range(len(minmaxDelimiters)):
        maxArray.append( int(parsedInput[i][minmaxDelimiters[i][1]+1:len(parsedInput[i])]) )  #input from the character after the delimiter to the end of the string

if(len(minArray) != len(maxArray)):
    print('Error: minArray and maxArray are not the same size!')
#/2

#3. Create an array idArray of all values (ids) between min and max, inclusive
idArray = [[-1, -1] for _ in range(len(minArray))] #Another 2D array, this time to hold all values between min and max for each entry in parsedInput
for i in range(len(minArray)):
    for j in range(minArray[i], maxArray[i] + 1):
        idArray[i] = list(range(minArray[i], maxArray[i] + 1))
        print('Adding value: ', j, ' to idArray[', i, ']')
    print('Run: ', i, 'of: ', len(minArray), ' - Next Max ', maxArray[i])

#Alright, now we can use the format idArray[x] to get all values between min and max for the xth entry in parsedInput
#/3

#4. Check the idArray from start to finish for repeating values.  Values can be a single character, or a phrase
#4a. So we will need to split up the word into a half-word chunk, then check that chunk against the whole.
repeatArray = []  #this will hold all the repeating values we find
for i in range(len(parsedInput)):
    ids = idArray[i]
    for j in range(len(ids)):
        word = str(ids[j])
        wordLength = len(word)
        chunk = word[0:wordLength//2]  #chunk is half the word, we use // in order to get an integer result
        chunkRepeat = chunk + chunk
        if(word == chunkRepeat):
            repeatArray.append(word)       

#/4

#5. Output the sum of all repeating values found in step 4
sumRepeats = 0
for i in range(len(repeatArray)):
    sumRepeats += int(repeatArray[i])
print('Sum of all repeating values: ', sumRepeats)
#/5


