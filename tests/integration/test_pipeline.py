from integration.report_pipeline import ReportPipeline


pipeline = ReportPipeline()


result = pipeline.run(

    image_path=
    "dataset/MR/test/glioma/Te-gl_96.jpg",

    modality="MR",

    patient_id=1,

    file_name="Te-gl_96.jpg"

)


print("=" * 60)
print("FINAL PIPELINE RESULT")
print("=" * 60)


print(result)


print("\n")


print("=" * 60)
print("PDF PATH")
print("=" * 60)


print(
    result["pdf"]["pdf_path"]
)


print("=" * 60)
print("STATUS")
print("=" * 60)


print(
    result["pdf"]["status"]
)