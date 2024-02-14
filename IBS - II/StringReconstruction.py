
import random

seq = "ATAGGCTACATGCG"
knum = int(input("Enter k-mer size: "))

kmerlist = [seq[i:i+knum] for i in range(0, len(seq) - knum + 1)]
kmerlist.sort()
print(kmerlist)

copykmer = [i for i in kmerlist]

sequence = random.choice(kmerlist)  
copykmer.remove(sequence)
print(sequence)

iterations = 0

while copykmer:
    prefix = [j[:2] for j in copykmer]
    suffix = [j[1:] for j in copykmer]

    rand = random.randint(0, 1)

    if rand == 0:
        if sequence[-2:] in prefix:
            index = prefix.index(sequence[-2:])
            collected = copykmer[index]
            prefix.pop(index)
            suffix.pop(index)
            sequence += collected[2]
            copykmer.remove(collected)

    if rand == 1:
        if sequence[0:2] in suffix:
            index = suffix.index(sequence[0:2])
            collected = copykmer[index]
            prefix.pop(index)
            suffix.pop(index)
            sequence = collected[0] + sequence
            copykmer.remove(collected)

    print(sequence)
    print(copykmer)

    iterations += 1

print("Number of iterations taken :", iterations)