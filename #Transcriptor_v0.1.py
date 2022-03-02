#Transcriptor v0.1
    #Transcriptor allows the user to input a genetic sequence (DNA), tells you the number of bp's
    #and outputs the DNA strand, its complement, and the RNA sequence
    #future versions of this program will allow the user to input an RNA sequence originally, as well as 
    #allow the program to read the codons of the sequence and output a protein strand
    #future versions will also you to insert capital letters lmfao


#Introduce and get DNA
print("Hello, welcome to the Transcriptor.")
DNASequence = input("Please enter your DNA sequence: ")
print("Your sequence contains", len(DNASequence) ,"base pairs. \n")

#First, print the original DNA sequence
print("Original Sequence: ", DNASequence, "\n")

#Second, output the complementary DNA strand
ComplementarySequence = ""
for x in DNASequence:
    if x == "a":
        ComplementarySequence = ComplementarySequence + "t"
    if x == "t":
        ComplementarySequence = ComplementarySequence + "a"
    if x == "g":
        ComplementarySequence = ComplementarySequence + "c"
    if x == "c":
        ComplementarySequence = ComplementarySequence + "g" 
print("Complementary Sequence: ", ComplementarySequence, "\n")

#Third, print the RNA sequence 
RNASequence = ""
for x in DNASequence:
    if x == "a":
        RNASequence = RNASequence + "u"
    if x == "t":
        RNASequence = RNASequence + "a"
    if x == "g":
       RNASequence = RNASequence + "c"
    if x == "c":
        RNASequence = RNASequence + "g"
print("RNA Sequence: ", RNASequence, "\n")
