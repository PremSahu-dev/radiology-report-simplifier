import pydicom
import matplotlib.pyplot as plt

# Replace with your DICOM file path
dicom_path = "imgMR1.dcm"

# Read DICOM file
dataset = pydicom.dcmread(dicom_path)

image = dataset.pixel_array

'''print(dataset)'''
print("Patient ID :", dataset.PatientID)
print("Modality   :", dataset.Modality)
print("Rows       :", dataset.Rows)
print("Columns    :", dataset.Columns)

print(image.shape)

plt.imshow(image, cmap="gray")
plt.title("DICOM Image")
plt.axis("off")
plt.show()

print(dataset.Modality)
