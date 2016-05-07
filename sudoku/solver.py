'''
Created on May 1, 2016

@author: anishsingh1
'''

import sys
import copy



def solve(puz):  
    
    p = solveByCrossHatching(puz)
    done = is_solved(p)
    
    if not done:
        done = solveByPickingOneOfTwoValues(p)
        
    if not done:
        done = solve_recursive(p,0)
        
    if not done:
        print 'cannot solve the puzzle'
            
            
                    
def solveByPickingOneOfTwoValues(p):
    
    p2 = getGridWithPossibleValuesInEachCell(p)
       
    done = False 
    r, c = 0,0
    while r < 9 and not done:
        while c < 9 and not done:
            if len(p2[r][c]) == 2:
                for v in p2[r][c]:
                    p_temp = copy.deepcopy(p)
                    p_temp[r][c] = [v]
                    p_s = solveByCrossHatching(p_temp)
                    done = is_solved(p_s)
                    if done: 
                        break
            c += 1
        r += 1
    return done


def solve_recursive(puz, rec_count):
    
#    if rec_count > 10: return False
    
    p = getGridWithPossibleValuesInEachCell(puz)
    
    # find cell with 2 possible values
    found = False
    r,c = 0,0
    for r in range(9):
        for c in range(9):
            if len(p[r][c]) == 2:  
                found = True
                break
        if found:
            break
        
    
      
    done = False
    if found:
        for v in p[r][c]:
            if not done:
                print "Using Cell rec_num= %d r=%d, c=%d cell_vals=%s v=%s" %(rec_count,r,c,p[r][c],v) 
                p_temp = copy.deepcopy(puz)
                p_temp[r][c] = [v]
                p_s = solveByCrossHatching(p_temp)
                done = is_solved(p_s)
                if not done:
                    #print "before recursion:"
                    #printPuzzle(p_temp)
                    done = solve_recursive(p_s, rec_count+1)
        
    return done

        
    
    
    # pick one cell with 2 possible values
    # for each possible value
    # create another grid with that value assigned to that cell
    # solve the puzzle with cross hatching
    # if not solved then do the same with next value of that cell
    # if still not solved.  pick one value for that cell
    # create another grid with that value assigned to that cell
    # call solve_recursive(new grid)
    # return solved or not

    
    

def solveByCrossHatching(puz):
    
    done = False
    #print "Input puzzle:"
    #printPuzzle(puz)
    
    while not done:
        #new_puz = [ [ '' for i in range(9) ] for j in range(9) ]
        new_puz = copy.deepcopy(puz)
        
        grid_with_values = getGridWithPossibleValuesInEachCell(puz)
        
        for r in range(9):
            for c in range(9):
                if len(grid_with_values[r][c]) == 1:
                    new_puz[r][c]= grid_with_values[r][c]
                    grid_with_values = getGridWithPossibleValuesInEachCell(new_puz)
                #else:
                #    new_puz[r][c]= puz[r][c]

        if isSame(puz, new_puz): 
            done = True
        else: 
            puz = new_puz
            #printPuzzle(puz)    

            
    #print "Output puzzle:"
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