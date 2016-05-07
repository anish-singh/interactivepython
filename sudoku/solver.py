'''
Created on May 1, 2016

@author: anishsingh1
'''

import sys
import copy



def solve(puz):  
    
    p = solveByCrossHatching(puz)
    done = is_solved(p)
    #done = False
    
    if not done:
        
        #done = solve_recursive(puz)
        p2 = getGridWithPossibleValuesInEachCell(p)
        
        curr_count = 2
        
        while curr_count < 3 and not done:
            r, c = 0,0
            while r < 9 and not done:
                while c < 9 and not done:
                    if len(p2[r][c]) == curr_count:
                        for v in p2[r][c]:
                            p_temp = copy.deepcopy(p)
                            p_temp[r][c] = [v]
                            p_s = solveByCrossHatching(p_temp)
                            done = is_solved(p_s)
                            if done: 
                                break
                    c += 1
                r += 1
            curr_count += 1

    if not done:
        print 'cannot solve the puzzle'
                    


def solve_recursive(puz):
    curr_count = 2
    done = False
    r, c = 0,0
    while r < 9 and not done:
        while c < 9 and not done:
            p = getGridWithPossibleValuesInEachCell(puz)
            if len(p[r][c]) == curr_count:
                for v in p[r][c]:
                    p_temp = copy.deepcopy(puz)
                    p_temp[r][c] = [v]
                    p_s = solveByCrossHatching(p_temp)
                    done = is_solved(p_s)
                    if not done:
                        done = solve_recursive(p_temp)
                    if done: 
                        break
    return done
    
    
    

def solveByCrossHatching(puz):
    
    done = False
    
    while not done:
        new_puz = [ [ '' for i in range(9) ] for j in range(9) ]
        
        grid_with_values = getGridWithPossibleValuesInEachCell(puz)
        
        for r in range(9):
            for c in range(9):
                if len(grid_with_values[r][c]) == 1:
                    new_puz[r][c]= grid_with_values[r][c]
                else:
                    new_puz[r][c]= puz[r][c]

        if isSame(puz, new_puz): 
            done = True
        else: 
            puz = new_puz
            
        printPuzzle(puz)
        
    return puz


def getGridWithPossibleValuesInEachCell(p):

    new_grid = [ [ '' for i in range(9) ] for j in range(9) ]
        
    allRowNums = initNumbersInAllRows(p)
    allColNums = initNumbersInAllCols(p)
    allGridNums = initNumbersInAllGrid(p)      
    for r in range(9):
        for c in range(9):
            if p[r][c][0]=='' :
                new_grid[r][c] = getAvailableValuesForCell(p, allRowNums[r], allColNums[c], allGridNums[r][c])       
            else:
                new_grid[r][c]= p[r][c]
    return new_grid



def getAvailableValuesForCell(p,rowNums, colNums, gridNums):
    values = []
    for i in range(1,10):
        s = str(i)
        if  s not in rowNums and \
            s not in colNums and \
            s not in gridNums and \
            s not in values:
            values.append(s)
    return values


def initNumbersInAllGrid(p):
    gridNums = []
    for r in range(9):
        gridNums.append([])
        for c in range(9):
            gridNums[r].append(getNumsInGrid(p, r, c))
    return gridNums
        

def initNumbersInAllRows(p):
    rowNums = []
    for r in range(9):
        l = getNumbersInRow(p,r)
        rowNums.append(l)
    return rowNums

def initNumbersInAllCols(p):
    colNums = []
    for c in range(9):
        l = getNumbersInCol(p,c)
        colNums.append(l)
    return colNums
        
def getNumbersInRow(p,r):
    l = []
    for i in p[r]:
        if i[0]!= '': 
            l.append(i[0])
    return l


def getNumbersInCol(p,c):
    l = []
    for i in range(9):
        if p[i][c][0] != '': 
            l.append(p[i][c][0])
    return l
    
def getNumsInGrid(p,r,c):
    r_base = r //3
    c_base = c //3
    l = []
    for i in range(3):
        for j in range(3):
            if p[r_base*3 + i][c_base*3 + j][0] != '': 
                l.append(p[r_base*3 + i][c_base*3 + j][0])
    return l    
    
def isSame(p1, p2):
    for i in range(9):
        for j in range(9):
            if p1[i][j] != p2[i][j]: return False
    return True
            
def is_solved(p):
    for i in range(9):
        for j in range(9):
            if len(p[i][j]) > 1 or p[i][j][0] == '': return False
    return True
            

def printPuzzle(p):
    for l in p:
        for r in l:
            if r == '': print ' ',
            else: print r,
        print
    print '-'*50
           


def readInput(filename):
    f = open(filename, 'rU')
    p = []
    
    for line in f:
        line = line.rstrip('\n')
        vals = line.split(',')
        if len(vals) != 9:
            print 'Error in input'
            sys.exit(1)
        r = [[x] for x in vals]
        p.append(r)
    return p
     
    


def main():
    
    args = sys.argv[1:]

    if not args:
        print 'usage: fileName'
        sys.exit(1)
    
    puz = readInput(args[0])
    printPuzzle(puz)
    solve(puz)
    
    

if __name__ == '__main__':
    main()