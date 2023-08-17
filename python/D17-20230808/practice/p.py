""" given  = [1,0,2,3,0,4,0,5,0]
res = []
for i in given: 
    if len(res) < len(given) : 

        if i == 0 and len(res) < (len(given)-1) :
                res+=[i,i]
        else: 
            res+=[i]
    
    else : 
          break

print('result', res) """

#outout  : 
# result [1, 0, 0, 2, 3, 0, 0, 4, 0, 0]

""" 
Write a function that takes a string as input and returns a dictionary containing the frequency 
of each word in the string.

Sample input :  str = "the quick brown fox jumps over the lazy dog the quick brown fox"
     Output :  {  'the': 2,  'quick': 2, 'brown': 2,     'fox': 2,     'jumps': 1,     'over': 1,     
     'lazy': 1,     'dog': 1 }

 """

""" str = "the quick brown fox jumps over the lazy dog the quick brown fox"

strList = str.split()

wordCount={}

for i in strList:
    if i in wordCount:
        wordCount[i] += 1
    else:
        wordCount[i] = 1
    
print(wordCount) """

# output : {'the': 3, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

""" 
Write a function that takes a list of integers as input and returns 
the largest difference between two Subsequent elements in the list

Sample input : nums_list = [2, 5, 8, 1, 9, 3, 7]
Output : 8 (9 - 1) 
"""

nums_list = [2, 5, 8, 1, 9, 3, 7]

