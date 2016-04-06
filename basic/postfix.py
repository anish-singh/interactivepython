'''
Created on Apr 5, 2016

@author: anishsingh1
'''


import MyDS

def convert_to_postfix(oper):
    
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    operators = '/*+-^'
    precedence = { '(':1, '+':2, '-':2, '/':3, '*':3, '^':4}
    s= MyDS.Stack()
    out = ''
   
    # if operand add to out.
    # if ( push to stack.
    # if ) pop symbols from stack until the last (. pop off las (
    # if operator pop operators in stack with higher or equal precedence and append to out. push operator to stack.
    # pop all operators from stack and append to out 
    
    tokens = getTokens(oper)
    
    for c in tokens:
        if c in operands or c.isdigit():  out = out + c + ' '
        elif c == '(': s.push(c)
        elif c in operators:
            while not s.isEmpty() and precedence[s.peek()] >=  precedence[c]:
                out = out + s.pop() + ' '
            s.push(c)
        elif c == ')':
            while not s.isEmpty() and not s.peek() == '(' :
                out = out + s.pop() + ' '
            s.pop()
            
    while not s.isEmpty():
        out = out + s.pop() + ' '
        
    return out
        

def eval_postfix(expr):
    
    tokens = getTokens(expr)  
    operators = '/*+-^'
    s = MyDS.Stack()
    
    for c in tokens:
        if c.isdigit() : s.push(c)
        elif c in operators:
            a = s.pop()
            b = s.pop()
            d = doMath(a,b,c)
            s.push(d)
            
    return s.pop()


             
def doMath(op1, op2, operation): 
#print str(op2) + "," + str(op1) + "," + operation
    if(operation == '*'): return int(op1) * int(op2)
    if(operation == '/'): return int(op2) / int(op1)
    if(operation == '+'): return int(op1) + int(op2)
    if(operation == '-'): return int(op2) - int(op1) 
    if(operation == '^'): return int(op2)**int(op1)         

def getTokens(s):
    
    count = 0
    tokens = []
    
    while count < len(s):
        ch = s[count]
                
        if ch.isdigit():
            num = ch
            count += 1
            
            while s[count].isdigit() and count < len(s) :
                num = num + s[count]
                count += 1
                
            tokens.append(num)
        else:
            tokens.append(ch)
            count += 1
        
        
        
    return tokens       
        

def main():

    print convert_to_postfix('10 + 3 * 5 / (16 - 4)')
    print eval_postfix("17 10 + 3 * 9 /")
    print convert_to_postfix('5 * 3 ^ (4 - 2)')
  
    
if __name__ == '__main__':
    main()