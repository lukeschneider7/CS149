"""Lab 8 Roses lab.

Author: Luke Schneider
Version: 09/27/23
I got help for this assignment in CS-149 on 09/27/2023
"""

if __name__ == '__main__':
    
    """ Rose Variables """
    rose1 = (2, 4, 3)
    rose2 = (5, 1, 2)
    rose3 = (5, 7, 2)
    rose4 = (1, 1, 10)
    rose5 = (1, 1, 1)
    
    bud = '@'
    stem = '-'
    thorn = '>'
    
    lengths = [rose1[0] + rose1[1] + rose1[2],
              rose2[0] + rose2[1] + rose2[2],
              rose3[0] + rose3[1] + rose3[2],
              rose4[0] + rose4[1] + rose4[2],
              rose5[0] + rose5[1] + rose5[2]]
    lengths.sort()
    longest = lengths[-1] + 3
    print(lengths)
    print(longest)
            
    rose1output = bud + stem * rose1[0] + thorn +stem * rose1[1] + thorn + stem * rose1[2]
    print(rose1output.rjust(longest))
    
    rose3output = bud + stem * rose3[0] + thorn +stem * rose3[1] + thorn + stem * rose3[2]
    print(rose3output.rjust(longest))
   
    

