dna=["A","G","T","C","G","A","T","C","T","T","U","G","T","G","C","C","T","A"]

threshold1="A"
threshold2="G"
threshold3="T"
threshold4="C"
threshold5="U"
threshold6="V"

adenine_present=False

for element in dna:
    if element==threshold1:
        adenine_present=True
        print("A")
    else:
            print("No A")

guanine_present=False

for element in dna:
    if element==threshold2:
        guanine_present=True
        print("G")
    else:
            print("No G")

thiamine_present=False

for element in dna:
    if element==threshold3:
        thiamine_present=True
        print("T")
    else:
        print("No T")

cytosine_present=False

for element in dna:
    if element==threshold4:
        cytosine_present=True
        print("C")
    else:
        print("No C")

urasile_present=False

for element in dna:
    if element==threshold5:
        urasile_present=True
        print("U")
    else:
        print("No U")

unknown_V_present=False

for element in dna:
    if element==threshold6:
        unknown_V_present=True
        print("V")
else:
    print("No unknown V")
