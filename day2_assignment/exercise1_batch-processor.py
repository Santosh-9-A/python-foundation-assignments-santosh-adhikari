'''Use a for loop and range() to print batch numbers from 1 to 10.

After every third batch, display:

Checkpoint reached
Example:

Processing batch 1
Processing batch 2
Processing batch 3
Checkpoint reached
Hint:

Use the modulo operator.

batch_number % 3 == 0'''

for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")


    if batch_number % 3 ==0:
        print("Checkpoint reached")

