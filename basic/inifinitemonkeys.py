'''
Created on Apr 3, 2016

@author: anishsingh1
'''

import random

target = "methinks it is like a weasel"
#target = "ab"
letters = 'abcdefghijklmnopqrstuvwzyz '
size = len(letters)
matched_chars = [0]*len(target)
curr_best_str = [" "]*len(target)

def main():
    
    nomatch = True
    while nomatch:
    
        string = generate()
    
        s = score(string)
    
        if s == 100 :
            print "matched: %s" %string
            nomatch = False
        else :
            print "returned string, target : %s, %s" % (string, target)
        
    

def generate():
    ''' generate a random string of len(target) with any of 26 + 1 characters '''
    
    # find the first non matched char in matched_chars
    # generate a random char for that position.
    # set curr_best_str to this value
    i = matched_chars.index(0)
    
    l = letters[random.randrange(size)]
    curr_best_str[i] = l

    if target[i] == l :
        matched_chars[i] = 1
    
#    ret_val = []
#    for i in range(length) :
#        ret_val.append(letters[random.randrange(size)])
        
    return ''.join(curr_best_str)
    
    
def score(input_str):
    if input_str == target:
        return 100
    else:
        return 0



if __name__ == '__main__':
    main()