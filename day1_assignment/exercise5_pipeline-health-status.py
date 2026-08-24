'''Given:

rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18
Calculate the failure rate.

Use these rules:

Healthy: Failure rate is at most 2% and runtime is at most 20 minutes.
Warning: Failure rate is more than 2% but at most 5%.
Critical: Failure rate is more than 5%.
Display the failure rate and final pipeline status.

Test it with:

rows_loaded = 9500
rows_failed = 500
runtime_minutes = 15
Then test:

rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30
“Think carefully about the final case.

The failure rate is low, but the runtime is high.

Should it still be classified as healthy?”'''

rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

print(f"Failure Rate: {failure_rate:.2f}%")
print("Pipeline Status:", status)

