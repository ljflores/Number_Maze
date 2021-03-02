import time

#--------Location -- structured as nodes----------#
class location:
    def __init__(self, row, col, data):
        self.children = {}
        self.row = row
        self.col = col
        self.data = data
        self.active = True
#-------------------------------------------------#
        
        
#---------Call this function----------------------#
def hw3(fileName):

    #-------Read the file-------------------------#
    file = open(fileName, 'r') 
    lines = file.readlines()
    #---------------------------------------------#

    n = int(lines[0]) # accessing n, the length of the matrix
    restOfLines = lines[1:(n*n)+1] # getting the rest of the lines
    file.close()

    # START TIME
    startTime = time.time()
    #----Create a matrix of locations-------------#
    matrix = []
    i = 1
    rowNum = 0
    while (i < n*n):
        nodeRow = []
        row = lines[i:(i+n)] # accessing a specific row
        
        colNum = 0
        for j in row:
            nodeRow.append(location(rowNum, colNum, int(row[int(colNum)])))
            colNum = colNum+1
            
        matrix.append(nodeRow)

        i = i + n
        rowNum = rowNum + 1

    #-----Adjacency matrix--------------------#
    for row in matrix:
        for a in row:
            a.active = False
            neighbors = []
            if ( (((a.col+a.data) >= 0) and ((a.col+a.data) < n)) and (matrix[a.row][a.col+a.data].active == True) and (matrix[a.row][a.col+a.data].data != 0) ):
                neighbors.append(matrix[a.row][a.col+a.data])
        
            #Check to see if you can safely move left
            if ( (((a.col-a.data) >= 0) and ((a.col-a.data) < n)) and (matrix[a.row][a.col-a.data].active == True) and (matrix[a.row][a.col-a.data].data != 0) ):
                neighbors.append(matrix[a.row][a.col-a.data])

            #Check to see if you can safely move down
            if ( (((a.row+a.data) >= 0) and ((a.row+a.data) < n)) and (matrix[a.row+a.data][a.col].active == True) and (matrix[a.row+a.data][a.col].data != 0) ):
                neighbors.append(matrix[a.row+a.data][a.col])

            #Check to see if you can safely move up
            if ( (((a.row-a.data) >= 0) and ((a.row-a.data) < n)) and (matrix[a.row-a.data][a.col].active == True) and (matrix[a.row-a.data][a.col].data != 0) ):
                neighbors.append(matrix[a.row-a.data][a.col])

            for i in range(0, len(neighbors)):
                a.children[neighbors[i]] = neighbors[i]


#------------------------------
    # Create adjacency dictionary
    Dict = {}
    i = 0
    while( i < len(matrix)):
        j = 0
        while (j < len(matrix[i])):
            key = matrix[i][j]
            Dict[key] = key.children
            j = j + 1   
        i = i + 1


    # Create a BFS dictionary
    Dict2 = {}
    Dict2[0] = {matrix[0][0]}
    
    i = 0
    while(i in Dict2):
        if (matrix[n-1][n-1] in Dict2[i]):
            break
        for elem in list(Dict2[i]):
            if (i+1) in Dict2:
                Dict2[i+1].update(Dict[elem])
            else:
                Dict2[i+1] = Dict[elem]
        i = i + 1

    message = "Path not found."
    # Find the earliest occurence.
    if (matrix[n-1][n-1] in Dict2[len(Dict2)-1]):
        message = "Shortest path is {} moves.".format(len(Dict2)-1)
    print(message)
    print("Time = {} ms".format((time.time()-startTime)*1000))

#--------------------------------------------------------#


