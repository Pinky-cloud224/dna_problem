dna="5'TACCGCAATTATATGC3'"

print("Length of DNA Sample",len(dna))

###############################################################

dna_sample="AGGGTCCTAHCGHTAVCGTACHHTCGGTCA"

valid_dna=["A","G","T","C"]

for element in dna_sample:
    if element not in valid_dna:
        print("Mutation")
    else:
        print("NO Mutation")

#ANOTHER WAY:
dna_sample="AGGGTCCTAHCGHVVTACGTAUUUUURRRRRCHHTCGGTCA"

valid_dna=["A","G","T","C"]

invalid_dna=[]

for element in dna_sample:
    if (element not in valid_dna) and (element not in invalid_dna):
        mutation=invalid_dna.append(element)
        print(invalid_dna)

#ANOTHER WAY:
dna_sample="AGGGTCCTAHCGHVVTACGTAUUUUURRRRRCHHTCGGTCA"

valid_dna=["A","G","T","C"]

for element in dna_sample:
    if element not in valid_dna:
        print(element)

############################################
#DNA MUTATION PROBLEM

actual_dna_sample="5'AATTTCCTTCATCTACTTGGCCTACATTCCAAA3'"
mutated_dna_sample="5'AATTUCCTTCATCTACTTGGACTACATTCTAAA3'"

for index in range(len(actual_dna_sample)):
    if actual_dna_sample[index]!=mutated_dna_sample[index]:
        print(actual_dna_sample[index],mutated_dna_sample[index],index)


#for index in range (0,len(actual_dna_sample),1):
    #print(actual_dna_sample[index])

#for index in range (2,len(actual_dna_sample),3):
    #print(actual_dna_sample[index])
