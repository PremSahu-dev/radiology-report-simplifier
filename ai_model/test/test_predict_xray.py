from inference.predict_xray import predict

result = predict("/home/kali/Downloads/000001.dcm")

print("=" * 50)
print("Top Prediction")
print("=" * 50)
print(result["prediction"])

print()

print("=" * 50)
print("Top 5 Findings")
print("=" * 50)

for item in result["all_predictions"][:5]:
    print(item)

print()

print("=" * 50)
print("AI Report")
print("=" * 50)
print(result["report"])

print("\n==================================================")
print("Grad-CAM")
print("==================================================")

print(result["gradcam_path"])
