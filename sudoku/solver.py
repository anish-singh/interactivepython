'''
Created on May 1, 2016

@author: anishsingh1
'''

import sys
import copy


def solve(puz):  
    
    p = solveByCrossHatching(puz)
    done = isSolved(p)

    if not done:
        done = solve_recursive(p,0)
        
    if not done:
        print 'cannot solve the puzzle'
            
            

def solve_recursive(puz, rec_count):
    
    #if rec_count > 5: return False
        
    p = getGridWithPossibleValuesForEachCell(puz)
    
    # find first cell with 2 possible values
    found = False
    for r in range(9):
        for c in range(9):
            if len(p[r][c]) == 2:  
                found = True
                break
        if found: break
        
    
    # solve by putting each possible value in the cell.
    # recurse. first recurse for value which results in fewer empty cells.
    
    done = False
    if found:
        
        print "Using Cell rec_num= %d r=%d, c=%d cell_vals=%s" %(rec_count,r,c,p[r][c]) 

        v1 = p[r][c][0]
        v2 = p[r][c][1]
        p_temp1 = copy.deepcopy(puz)        
        p_temp1[r][c] = [v1]
        ps1 = solveByCrossHatching(p_temp1)
        if isSolved(ps1): return True
        
        p_temp2 = copy.deepcopy(puz)        
        p_temp2[r][c] = [v2]
        ps2 = solveByCrossHatching(p_temp2)
        if isSolved(ps2): return True
        
        n1 = getNumOfUnSolvedCells(ps1)
        n2 = getNumOfUnSolvedCells(ps2)
        
        if n1 >= n2:
            done = solve_recursive(ps2, rec_count+1)
            if not done:
                done = solve_recursive(ps1, rec_count+1)
        else:
            done = solve_recursive(ps1, rec_count+1)
            if not done:
                done = solve_recursive(ps2, rec_count+1)
    return done


    
    

def solveByCrossHatching(puz):
    
    done = False

    while not done:

        new_puz = copy.deepcopy(puz)
        
        grid_with_values = getGridWithPossibleValuesForEachCell(puz)
        
        for r in range(9):
            for c in range(9):
                if len(grid_with_values[r][c]) == 1:
                    new_puz[r][c]= grid_with_values[r][c]
                    grid_with_values = getGridWithPossibleValuesForEachCell(new_puz)

        if isSame(puz, new_puz): 
            done = True
        else: 
            puz = new_puz

    printPuzzle(puz)    
    return puz



def getNumOfUnSolvedCells(p):
    count = 0
    for r in range(9):
        for c in range(9):
            if p[r][c][0]=='' :
                count += 1
    return count

    
    
def getGridWithPossibleValuesForEachCell(p):

    new_grid = copy.deepcopy(p)
        
    allRowNums = getNumbersInAllRows(p)
    allColNums = getNumbersInAllCols(p)
    allGridNums = getNumbersInAllGrids(p)      
    for r in range(9):
        for c in range(9):
            if p[r][c][0]=='' :
                new_grid[r][c] = getAvailableValuesForCell(p, allRowNums[r], allColNums[c], allGridNums[r][c])       
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


def getNumbersInAllGrids(p):
    gridNums = []
    for r in range(9):
        gridNums.append([])
        for c in range(9):
            gridNums[r].append(getNumsInGrid(p, r, c))
    return gridNums
        

def getNumbersInAllRows(p):
    rowNums = []
    for r in range(9):
        l = getNumbersInRow(p,r)
        rowNums.append(l)
    return rowNums

def getNumbersInAllCols(p):
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
            
def isSolved(p):
    for i in range(9):
        for j in range(9):
            if p[i][j][0] == '': return False
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