seq1 = "TAGCC"
seq2 = "GCCATGC"
n1 = len(seq1); n2 = len(seq2)
matrix = [[0]*n2 for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        if seq1[i]==seq2[j]:
            matrix[i][j] = 1
for i in matrix:
    print(i)

