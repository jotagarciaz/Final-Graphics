def convertToL(mat, pos):
    pos=pos*9

    for i in range (5):
        mat[pos+2][i]=0
        mat[pos+3][i]=0
        mat[pos+4][i]=0
        mat[pos+5][i]=0
        mat[pos+7][i]=0
        mat[pos+8][i]=0

    return mat