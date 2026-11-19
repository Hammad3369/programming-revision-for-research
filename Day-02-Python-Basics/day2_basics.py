# The basic if function:
lenght = 150

if lenght > 100:
    print("long sequence")

# Indentation: it is very important in python, python uses to understand which code is belong to the "if"

if lenght > 100:
    print("long sequence")

lenght = 150
if lenght == 100:
    print("long sequence")

print("python is working")

lenght = 80
if lenght > 100:
    print("long sequence")
else:
    print("short sequence")

# elif: Sometimes there are more than two possibilities

lenght = 500

if lenght < 100:
    print("Short")

elif lenght < 500:
    print("short")

else:
    print("long")

# Logical operators : Sometimes you need multiple conditions, python has and, or, and not

length = 500
gc_content = 55

if length > 100 and gc_content > 50: # in this case both condition will be true.
    print("meets criteria")

if length > 100 or gc_content > 50:
    print("Interesting sequence")

# Reverses True/false
is_valid = True

if not is_valid:
    print("Invalid")

dna = "Atgc"
# print(dna[0])
# print(dna[1]) Instead of using this again and again we should used loop
# print(dna[2])
# print(dna[3])

for base in dna:
    print(base)

#Loop and Condition

dna = "ATGCGT"

for base in dna:

    if base == "G":
        print("Found G")

# Range
for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

# Enumerate function
dna = "Atgc"
for i in range(len(dna)): # to note the position and base
    print(i, dna[i])

# Sometimes you want to break the stop the loop

dna = "ATGCGT"

for base in dna:
    if base == "G":
        break

    print(base)

# Continue : Skipping the iteration and continue with nxt one

dna = "ATGCGT"

for base in dna:

    if base == "G":
        continue

    print(base)

# While Loop: A while loop repeats while condition is true

count = 0

while count < 5:
    print(count)   # Finite loop

    count += 1

# Infinite Loop

count = 0

while count < 5:

    break 
    print(count)
    count += 1

print("python is working")

# Functions : are usable block of code

def greet():
    print("Hello") # Simple function
greet()

# Function with parameter:

def greet(name):
    print(f"hello {name}")

greet("Hammad")

# Function + return
def add(a, b):
    result = a + b

    return result  # Important note; print() function shows something on the screen and "return" sent results back to the  program.
answer = add(5, 3)
print(answer)

print("Python is working")

# Better Example ---  GC Content Counting

def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")

    total = len(sequence)
    return (g + c) / total * 100

dna = "ATGCGT"
gc = gc_content(dna)
print(gc)

# Now we can put everything together, by upgading day 1 Fasta parser

# first create function
def parse_fasta(fasta):
   sequences = {}
   current_id = None

   for line in fasta.split("\n"):

    line = line.strip()

    if line.startswith(">"):
        current_id = line[1:]
        sequences[current_id] = ""

    else:
        sequences[current_id] += line

   return sequences

fasta = """>seq1
ATGCGT
>seq2
GGGAAA"""

sequences = parse_fasta(fasta)

print(sequences)

# Bioinformatics Example
def sequence_Length(sequence):
    return len(sequence)

dna = "ATGCGT"
Length = sequence_Length(dna)

print(Length)