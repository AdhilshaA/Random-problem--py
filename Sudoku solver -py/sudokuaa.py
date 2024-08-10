#My Sudoku solver

#datastructure

sgrid1 = {0: [0, 6, 7, 3, 0, 0, 0, 0, 9], 1: [0, 5, 0, 0, 0, 0, 1, 0, 6], 2: [9, 0, 0, 0, 0, 5, 0, 0, 0], 3: [0, 0, 0, 0, 2, 0, 4, 0, 8], 4: [5, 8, 0, 0, 0, 0, 0, 2, 1], 5: [7, 0, 4, 0, 9, 0, 0, 0, 0], 6: [0, 0, 0, 2, 0, 0, 0, 0, 4], 7: [2, 0, 5, 0, 0, 0, 0, 1, 0], 8: [1, 0, 0, 0, 0, 9, 5, 7, 0]}
sgrid2 = {0: [0, 0, 0, 0, 8, 7, 3, 0, 9], 1: [0, 0, 0, 9, 0, 6, 0, 0, 0], 2: [0, 4, 5, 0, 0, 0, 0, 0, 0], 3: [0, 0, 4, 8, 0, 0, 6, 0, 5], 4: [2, 8, 0, 0, 0, 0, 0, 9, 1], 5: [5, 0, 6, 0, 0, 1, 7, 0, 0], 6: [0, 0, 0, 0, 0, 0, 5, 6, 0], 7: [0, 0, 0, 3, 0, 8, 0, 0, 0], 8: [4, 0, 8, 5, 6, 0, 0, 0, 0]}
sgrid3 = {0: [1, 0, 7, 8, 0, 0, 6, 0, 4], 1: [0, 0, 2, 0, 9, 5, 0, 1, 0], 2: [0, 0, 0, 0, 0, 4, 3, 0, 0], 3: [0, 9, 0, 0, 7, 0, 5, 0, 3], 4: [0, 1, 5, 2, 0, 3, 9, 8, 6], 5: [0, 8, 0, 0, 0, 0, 4, 7, 1], 6: [0, 0, 1, 4, 2, 9, 0, 6, 0], 7: [0, 4, 0, 0, 8, 1, 0, 0, 0], 8: [0, 0, 0, 0, 0, 7, 1, 4, 0]}

changes = 0
pchanges = 0

pgrid={}
for i in range(9):
    if 0 in sgrid[i]: pgrid[i]=dict()

vchart = dict()
for i in range(9):
    vchart[i+1]={'g':[0,1,2,3,4,5,6,7,8],'r':[0,1,2,3,4,5,6,7,8],'c':[0,1,2,3,4,5,6,7,8]}

gchart={}
for num in range(1,10):
    gchart[num]={}

gcorrected={}
for i in range(1,10):
    gcorrected[i]={'sgrid':[],'drow':[],'dcol':[]}
# functions neededd

#function for finding which grid it belongs to
def gvalue(r,c):
    return (((r // 3) * 3) + (c // 3))

#function to print a sudoku grid
def printsgrid():
    for key in sgrid.keys():
        for n in sgrid[key]:
            print(n,'',end='')
        print('')

#function to print a pencil grid
                    
                    
            
        
            
#the one and only super pencil function
#--------------------------------------


def superpencil():    

    #setting a blank space grid
        
    for i in range(9):
        for j in range(9):
            if sgrid[i][j] == 0:
                pgrid[i][j]=list()
    #filling the vacancy chart from the sgrid
            else:
                vchart[(sgrid[i][j])]['r'].remove(i)
                vchart[(sgrid[i][j])]['c'].remove(j)
                vchart[(sgrid[i][j])]['g'].remove(gvalue(i,j)) #could make a vchart update fn. or vchart making fn.
    #filling the blank grid one by one
    for row in pgrid.keys():
        for column in pgrid[row].keys():
            for i in range(1,10):
                if row in vchart[i]['r'] and column in vchart[i]['c'] and gvalue(row,column) in vchart[i]['g']:
                    pgrid[row][column].append(i)


#removing the pgrid lines if fully filled
def pgridlinecheck():
    for i in range(9):
        if i in pgrid.keys() and pgrid[i].keys() == []:
            del pgrid[i]

    
#function for updating a single number in gchart
def gchartupdate(num):
    try: del gchart[num]
    except: pass    
    gchart[num]={}
    for i in range(9):
        gchart[num][i]={'r':[0,0,0],'c':[0,0,0]}
    for r in range(9):
        for c in pgrid[r].keys():
            if num in pgrid[r][c]:
                g = gvalue(r,c)
                gchart[num][g]['r'][r // 3] = 1
                gchart[num][g]['c'][c // 3] = 1

    
#fn. for building gchart - onetime                
def gchart_build():                
    for i in range(1,10):
        gchartupdate(i)


#To remove the single line corrections in a single grid
def pencilcorrectsingle(num):
    newpchanges = 0
    for g in range(9):
        if g in gcorrected[num]['sgrid']:
            continue
        countr = 0
        countc = 0
        row = None
        col = None
        for i in range(3):
            if gchart[num][g]['r'][i] == 1:
                countr += 1
                row = i
            if gchart[num][g]['c'][i] == 1:
                countc += 1
                col = i
        if countr == 1:
            row = ((g // 3) * 3) + row
            for c in pgrid[row].keys():
                if num in pgrid[row][c] and gvalue(row,c) != g:
                    pgrid[row][c].remove(num)
                    newpchanges += 1
                    gcorrected[num]['sgrid'].append(g)
                    if (g // 3) not in gcorrected[num]['drow']: gcorrected[num]['drow'].append(g // 3)
        if countc == 1:
            col = ((g % 3) * 3) + col
            for r in range(9):
                if col in pgrid[r].keys() and num in pgrid[r][col] and  gvalue(r,col) != g:
                    pgrid[r][col].remove(num)
                    newpchanges += 1
                    gcorrected[num]['sgrid'].append(g)
                    if (g % 3) not in gcorrected[num]['dcol']: gcorrected[num]['dcol'].append(g % 3)
    return newpchanges


#To remove the double line corrections
def pencilcorrectdouble(num):
    newpchanges = 0
    for gref in range(3):
        if gref not in gcorrected[num]['drow']:
            countr = [0,0,0]
            row = [0,0,0]
            for g in [((gref * 3) + j) for j in range(3)]: 
                for i in range(3):
                    if gchart[num][g]['r'][i] == 1:
                        countr[g % 3] += 1
                    else: row[g % 3] = i

            if countr[0] == 2:
                if countr[1] == 2:
                    gcorrected[num]['sgrid'].append((gref * 3) + 2)
                    if gref not in gcorrected[num]['drow']: gcorrected[num]['drow'].append(gref)
                    for r in [k for k in range((gref * 3),(gref * 3) + 3) if k in pgrid.keys() and (k % 3) != row[0]]:
                        for c in [l for l in range(6,9) if l in pgrid[r].keys()]:
                            try:
                                pgrid[r][c].remove(num)
                                newpchanges += 1
                            except: pass
                    break
                                
                elif countr[2] == 2:
                    gcorrected[num]['sgrid'].append((gref * 3) + 1)
                    if gref not in gcorrected[num]['drow']: gcorrected[num]['drow'].append(gref)
                    for r in [k for k in range((gref * 3),(gref * 3) + 3 ) if k in pgrid.keys() and  (k % 3) != row[0]]:
                        for c in [l for l in range(3,6) if l in pgrid[r].keys()]:
                            try:
                                pgrid[r][c].remove(num)
                                newpchanges += 1
                            except: pass
                    break
            elif countr[1:] == [2,2]:
                gcorrected[num]['sgrid'].append(gref * 3)
                if gref not in gcorrected[num]['drow']: gcorrected[num]['drow'].append(gref)
                for r in [k for k in range((gref * 3),(gref * 3) + 3) if k in pgrid.keys() and  (k % 3) != row[1]]:
                    for c in [l for l in range(0,3) if l in pgrid[r].keys()]:
                        try:
                            pgrid[r][c].remove(num)
                            newpchanges += 1
                        except: pass

        if gref not in gcorrected[num]['dcol']:
            countc = [0,0,0]
            col = [0,0,0]
            for g in [((j * 3) + gref) for j in range(3)]:
                if gchart[num][g]['c'][i] == 1:
                    countc[g // 3] += 1
                else: col[g // 3] = i            
            if countc[0] == 2:
                if countc[1] == 2:
                    gcorrected[num]['sgrid'].append(6 + gref)
                    if gref not in gcorrected[num]['dcol']: gcorrected[num]['dcol'].append(gref)
                    for r in [k for k in range(6,9) if k in pgrid.keys()]:
                        for c in [l for l in range((gref * 3),(gref * 3) + 3) if l in pgrid[r].keys() and (l % 3) != col[0]]:
                            try: pgrid[r][c].remove(num)
                            except: pass
                    break
                                
                elif countr[2] == 2:
                    gcorrected[num]['sgrid'].append(3 + gref)
                    if gref not in gcorrected[num]['dcol']: gcorrected[num]['dcol'].append(gref)
                    for r in [k for k in range(3,6) if k in pgrid.keys()]:
                        for c in [l for l in range((gref * 3),(gref * 3) + 3) if l in pgrid[r].keys() and (l % 3) != col[0]]:
                            try: pgrid[r][c].remove(num)
                            except: pass
                    break
            elif countr[1:] == [2,2]:
                gcorrected[num]['sgrid'].append(gref)
                if gref not in gcorrected[num]['dcol']: gcorrected[num]['dcol'].append(gref)
                for r in [k for k in range(0,3) if k in pgrid.keys()]:
                        for c in [l for l in range((gref * 3),(gref * 3) + 3) if l in pgrid[r].keys() and (l % 3) != col[1]]:
                            try: pgrid[r][c].remove(num)
                            except: pass
    return newpchanges

#To fill if single in row
def fill_row(num):
    newchanges = 0
    removedr = []
    for r in vchart[num]['r']:
        count = 0
        for c in pgrid[r].keys():
            if num in pgrid[r][c]:
                count += 1
                sq = (r,c)
        if count == 1:
            sgrid[sq[0]][sq[1]] = num
            newchanges += 1
            removedr.append(r)
            del pgrid[sq[0]][sq[1]]
            for row in range(9):
                if sq[1] in pgrid[row].keys():
                    try: pgrid[row][sq[1]].remove(num)
                    except: pass
            g = gvalue(sq[0],sq[1])
            for row in range((g // 3) * 3, ((g // 3) * 3) + 3):
                for col in range((g % 3) * 3, ((g % 3) * 3) + 3):
                    if col in pgrid[row].keys():
                        try: pgrid[row][col].remove(num)
                        except: pass
            vchart[num]['g'].remove(g)
            vchart[num]['c'].remove(sq[1])
                
    for r in removedr:
        vchart[num]['r'].remove(r)

    return newchanges

#To fill if single in column
def fill_col(num):
    newchanges = 0
    removedc = []
    for c in vchart[num]['c']:
        count = 0
        for r in range(9):
            if c in pgrid[r].keys() and num in pgrid[r][c]:
                count += 1
                sq = (r,c)
        if count == 1:
            sgrid[sq[0]][sq[1]] = num
            newchanges += 1
            removedc.append(c)
            del pgrid[sq[0]][sq[1]]
            for column in pgrid[sq[0]].keys():
                try: pgrid[sq[0]][column].remove(num)
                except: pass
            g = gvalue(sq[0],sq[1])
            for row in range((g // 3) * 3, ((g // 3) * 3) + 3):
                for col in range((g % 3) * 3, ((g % 3) * 3) + 3):
                    if col in pgrid[row].keys():
                        try: pgrid[row][col].remove(num)
                        except: pass
            vchart[num]['g'].remove(g)
            vchart[num]['r'].remove(sq[0])
                
    for c in removedc:
        vchart[num]['c'].remove(c)

    return newchanges


#To fill if single in grid
def fill_grid(num):
    newchanges = 0
    removedg = []
    for g in vchart[num]['g']:
        count = 0
        for r in range((g // 3) * 3, (((g // 3) * 3) + 3)):
            if r not in pgrid.keys():
                continue
            for c in range((g % 3) * 3, (((g % 3) * 3) + 3)):
                if c in pgrid[r].keys() and num in pgrid[r][c]:
                    count += 1
                    sq = (r,c)
        if count == 1:
            sgrid[sq[0]][sq[1]] = num
            newchanges += 1
            removedg.append(g)
            vchart[num]['r'].remove(sq[0])
            vchart[num]['c'].remove(sq[1])
            del pgrid[sq[0]][sq[1]]
            for column in pgrid[sq[0]].keys():
                try: pgrid[sq[0]][column].remove(num)
                except: pass
            for row in range(9):
                if sq[1] in pgrid[row].keys():
                    try: pgrid[row][sq[1]].remove(num)
                    except: pass
                
    for g in removedg:
        vchart[num]['g'].remove(g)

    return newchanges


#Methods application-level fn.s
#------------------------------
        
#filling single in grid until no new changes
def run_grid(changes):
    while True:
        oldchanges = changes
        for i in range(1,10):
            newchanges = fill_grid(i)
            changes += newchanges
            while  newchanges != 0:
                newchanges = fill_grid(i)
                changes += newchanges
        if oldchanges == changes:
            break

def run_singlerowcol(changes):
    while True:
        oldchanges = changes
        for i in range(1,10):
            newchanges = fill_row(i)
            changes += newchanges
            while  newchanges != 0:
                newchanges = fill_row(i)
                changes += newchanges
            newchanges = fill_col(i)
            changes += newchanges
            while  newchanges != 0:
                newchanges = fill_col(i)
                changes += newchanges
        if oldchanges == changes:
            break
            
def simple_fill():
    while True:
        ancientchanges = changes
        run_grid(changes)
        run_singlerowcol(changes)
        if ancientchanges == changes:
            break
    pgridlinecheck()
    

def pencil_correct(pchanges):
    while True:
        gchart_build()
        oldpchanges = pchanges
        for i in range(1,10):
            newpchanges = pencilcorrectsingle(i)
            pchanges += newpchanges
            while newpchanges != 0:
                newpchanges = pencilcorrectsingle(i)
                pchanges += newpchanges
        if oldpchanges == pchanges:
            break
        
    while True:
        gchart_build()
        oldpchanges = pchanges
        for i in range(1,10):
            newpchanges = pencilcorrectdouble(i)
            pchanges += newpchanges
            while newpchanges != 0:
                newpchanges = pencilcorrectdouble(i)
                pchanges += newpchanges
        if oldpchanges == pchanges:
            break
            
    
    

    
    
    
    
            
        
                                   

#printing pgrid





#running stuff
#-------------

##print('\t\t--------------\n\t\tSUDOKU SOLVER\n\t\t--------------')
##print('\n\tInstructions\n\t------------')
##print('Enter the data with the following instructions:')
##print('\n * Each row data will be requested')
##print('* Enter the numbers in each  row without spaces in btw them')
##print('* Use  zero "0" instead of blank spaces in the puzzle')
##print("  e.g. Enter '105780029'")
##
##for i in range(9):
##    sgrid[i]=list(map(int,input('Enter {}th row:'.format(i+1))))

print('The entered puzzle is:')
printsgrid()
superpencil()

#hard level solver------------------------------------------
while True:
    grandchanges = changes
    grandpchanges = pchanges
    simple_fill()
    pencil_correct(pchanges)
    if grandchanges == changes and grandpchanges == pchanges:
        break
#-----------------------------------------------------------
print('\n \t\tSUCCESS!! \n The solved sudoku puzzle:')
printsgrid()




# TO DO
##* run once and see that 'changes value used before assignment'
##* include pchanges thingy in pcorrect functions


