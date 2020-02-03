def convertToT(mat, pos):
    pos=pos*9

    for i in range (5):
        mat[pos][i]=0
        mat[pos+1][i]=0
        mat[pos+3][i]=0
        mat[pos+4][i]=0
        mat[pos+5][i]=0
        mat[pos+6][i]=0

    return mat