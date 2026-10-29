import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Demo data for a simple data-drift monitoring report.
reference_data = pd.DataFrame({
    "age": [22, 25, 28, 30, 32, 35, 27, 29, 31, 26]
})
current_data = pd.DataFrame({
    "age": [45, 48, 52, 55, 60, 42, 50, 58, 47, 53]
})

report = Report([DataDriftPreset()])
snapshot = report.run(
    current_data=current_data,
    reference_data=reference_data
)
snapshot.save_html("evidently_report.html")

print("Evidently monitoring completed.")
print("Report saved as evidently_report.html")
