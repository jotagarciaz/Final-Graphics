def convertToM(mat, pos):
    pos=pos*9

    for i in range (5):
        mat[pos+5][i]=0
        mat[pos+6][i]=0
        mat[pos+8][i]=0

    return mat