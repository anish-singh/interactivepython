'''
Created on Apr 5, 2016

@author: anishsingh1
'''
import MyDS

def is_balanced(string):
 
    stack = MyDS.Stack()
    
    for s in string:
        if s == '(' or s == '[' or s == '{':  stack.push(s)
        elif s == ')' or s == ']' or s == '}': 
            if (stack.size() == 0):  return False
            else: 
                c = stack.pop()
                if s == ')' and c != '(': return False
                elif s == ']' and c != '[': return False
                elif s == '}' and c != '{': return False
    
    if stack.size() == 0 :  return True
    else: return False


def convert_to_base(num, base):
    
    digits = '0123456789ABCDEF'
    s = MyDS.Stack()
    
    while (num >0):
        s.push(num % base)
        num = num // base
        
    binVal = []
    while not s.isEmpty():
        binVal.append(digits[s.pop()])
    
    return ''.join(binVal)


if __name__ == '__main__':
    print is_balanced('[](()){[()]}')
    print convert_to_base(8,8)