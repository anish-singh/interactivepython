'''
Created on Apr 9, 2016

@author: anishsingh1
'''

import basic.MyDS

def reverseString(string):
    out = ''
    for i in range(len(string) -1, -1, -1):
        out += string[i]
        
    return out

def isPalindrome(s):
    r = reverseString(s)
    return r == s


def convertAnyBase(num, base):
    s = ""
    convertString = "0123456789ABCDEF"
    if num < base:  s += convertString[num]
    else:
        s = convertString[num %base] + s
        s = convertAnyBase(num//base, base) + s
    return s


def convertAnyBaseUsingStack(num, base):
    s = basic.MyDS.Stack()
    convertString = "0123456789ABCDEF"
    
    while num >0:
        if num < base:  
            s.push(convertString[num])
        else:
            s.push(convertString[num % base])
        num = num // base
          
    out = ''  
    while not s.isEmpty():
        out += s.pop()
        
    return out


def hanoi(num, frm, to, using):
    #print "h num=%d frm=%s to=%s using=%s" %(num, frm, to, using)
    if(num > 0):
        hanoi(num -1, frm,using, to)
        moveDisk(num,frm,to )
        hanoi(num -1, using, to, frm)
        

def moveDisk(n, frm, to):
    
    print 'Moving Disk %d from %s to %s' %(n,frm, to)

    

def main():
    #print convertAnyBaseUsingStack(9, 2)
    #print reverseString('hello')
    #print isPalindrome('radar')
    hanoi(3,'A','C', 'B')
    
    
if __name__ == '__main__':
    main()