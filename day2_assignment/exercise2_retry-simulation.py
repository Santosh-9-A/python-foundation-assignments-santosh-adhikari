'''Create a while loop that allows a maximum of three retry attempts.

Use variables such as:

attempt = 1
max_attempts = 3
operation_successful = False
For each attempt, print:

Attempt 1
Attempt 2
Attempt 3
Stop early using break if the operation succeeds.

After the loop, display either:

Operation completed successfully
or:

Operation failed after three attempts
Stretch:

Simulate success on the second attempt.'''

attempt = 1
max_attempts = 3
operation_successful = False

while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Simulate success on the second attempt
    if attempt == 2:
        operation_successful = True
        break

    attempt += 1

if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")