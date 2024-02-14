input = "ATAAGGCTACATGCG"
k_v=[3,4,5]
for k in k_v:
    seq=[]
    for i in range(len(input)-k+1):
        seq.append(input[i:i+k])
    print("Sequence of",k,"-mers:")
    print(sorted(seq))