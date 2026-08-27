'''Question 1 — Simple Interest Calculator (Default Arguments)

Write a function `calculate_simple_interest(principal, rate=5, time=1)` that calculates and
returns the simple interest using the formula:

```
interest = (principal * rate * time) / 100
```

- `rate` should default to `5` (percent) if not provided.
- `time` should default to `1` (year) if not provided.

**Sample calls and expected output:**
```python
calculate_simple_interest(1000, 10, 2)   # -> 200.0
calculate_simple_interest(1000)          # -> 50.0   (uses default rate=5, time=1)
calculate_simple_interest(2000, time=3)  # -> 300.0  (uses default rate=5)'''

def calculator_simple_interest(principal, rate=5, time=1):
    interst = (principal*rate*time)/100
    return interst


print(calculator_simple_interest(1000, 10, 2)  )
print(calculator_simple_interest(1000)  )        
print(calculator_simple_interest(2000, time=3))