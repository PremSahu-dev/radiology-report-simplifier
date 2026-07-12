from report_generator.report_generator import generate_report

report = generate_report(
    modality="MR",
    prediction="glioma",
    confidence=99.91
)

print(report)
