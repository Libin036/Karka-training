user_details = [
                
                {
                    "name" : "ajay",
                    "marks" : [80,90,70,40,60]
                },
                {
                    "name" : "manimala",
                    "marks" : [100,80,40,90,70]
                },
                {
                    "name" : "abarna",
                    "marks" : [72,65,68,89,86]
                }
        ]
        
        
        
for student in user_details:
    print(student['marks'])
    
    total = 0
    max_mark=student['marks'][0]
    
    for x in student['marks']: 
        total = total + x
        
        if x >= max_mark:
           max_mark = x 
            
    print('Total mark :',total)
    print('Max mark :',max_mark)