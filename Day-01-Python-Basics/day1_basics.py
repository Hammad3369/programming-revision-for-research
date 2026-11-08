# Variable = A container that stores information
name = "Hammad"
age =  25
print(name)
print(25)

# Whole numbers
gene_number = 50

# Float = decimal number
gc_content = 45.6

#string = collection of characters and text
# DNA sequence is string
# Protein sequence string
# gene name is  also string 

dna = "ATGCGT"

#Bool (boolean)
True
False
is_valid = True
print(is_valid)

# Checkiing the data type
dna = "ATCCCC"
print(type(dna))

# Changing one data type to another
# String to Integer
age = '25'
age = int(age)
print(age)

# Integer to String
number = 100
text = str(number)

#Strings
#String - Sequence of characters

dna = 'ATGCGT'
# Indexing 
dna[0]
dna[-1]

# Slicing: Getting a part of string
dna = "ATGCGT"
dna[0:3]
print(dna)

# important slicing method : bringing one string into mutliple strings

text = "DNA RNA Protein"
print(text.split())

letters = ["a", "t", "g"]
print("".join(letters))

print("  ATGC  ".strip())

# Python Collections

# 1. List[]
# Ordered + changeable
genes = ["BRCA1", "TP53", "MYC"]
print(genes[0])

# 2. Tuple()
# Ordered + cannot change , and used when data is fixed
position = (10, 20)

# 3. Unique values only
bases = {"a", "b", "c", "g", "a"}
print(bases) # Duplicate remove automatically

# Dictionary {}
gene = {
    "BRCA1" : "Human",
    "TP53" : "Human"
}
print(gene)

# Some are immutable which cannot change
list = [1,2,3]
list.append(4)
print(list)

# List Comprehension
# It is short way to create lists
numbers = []

for i in range(5):
    numbers.append(i)
print(numbers)

# Shortcut way
numbers=[i for i in range(5)]
print(numbers)

fasta = """>seq1
ATGCTGT
>seq2
GGGAAA"""

sequences={}

current_id=None

for line in fasta.split("\n"):
    line=line.strip()

    if line.startswith(">"):
        current_id=line[1:]

        sequences[current_id]=""
    else:
        sequences[current_id]+=line

print(sequences)













































































































































































































