dna_array=[
"A","T","G","C",
[
"AA","GG","TA",
[
"AAA","GAC","TAA","TCA","TTA","TCAG","TAC",
["AG","TC","GT","CT","TCAT"]
]
]
]

dna_array=["A","T","G","C",["AA","GG","TA",["AAA","GAC","TAA","TCA","TTA","TCAG","TAC",["AG","TC","GT","CT","TCAT"]]]]

print(dna_array[4][3][7][4])
remove=dna_array[4][3].pop(6)
print(dna_array)
remove=dna_array[4].pop(3)
print(dna_array)

dna_array[0]="UUUUUUUUUUU"
print(dna_array)

dna_array[4][2]="UAAAAAAAAAA"
print(dna_array)

####################################################################################

dna_sample="AGTCGTTACGGTAGCTCTACGTCTTTTTACGTCA"
rna_sample="ACTUCTUCCCTTAACUCTUCTACUUUTTCCAGTC"

threshold1="A"
threshold2="U"

adenine_present=False
uracile_present=False

for element in dna_sample:
    if element==threshold1:
        adenine_present=True
        if uracile_present:
            break
for element in rna_sample:
    if element==threshold2:
        uracile_present=True
        if adenine_present:
            break
print(adenine_present)
print(uracile_present)



##########################################################################################
#PYTHONIC RULES
dna_sample="AGTCGTTACGGTAGCTCTACGTCTTTTTACGTCA"
rna_sample="ACTUCTUCCCTTAACUCTUCTACUUUTTCCAGTC"

Adenine="A"
Uracile="U"

if Adenine in dna_sample:
    print("Adenine is present")
else:
    print("Nothing")


if Uracile in rna_sample:
    print("Uracile is present")
else:
    print("Nothing")



#############################################################################################
