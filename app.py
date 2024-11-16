import streamlit as st
import pydicom
import matplotlib.pyplot as plt
import numpy as np
import cv2
import io

# Define a function to display DICOM metadata, omitting unavailable attributes
def display_metadata(dicom_data):
    metadata_keys = [
        "PatientID", "SOPInstanceUID", "ContentDate", "ContentTime",
        "SeriesDescription", "FileMetaInformationVersion", "MediaStorageSOPClassUID",
        "MediaStorageSOPInstanceUID", "TransferSyntaxUID", "ImplementationClassUID",
        "ImplementationVersionName", "SliceThickness", "SpacingBetweenSlices",
        "PatientPosition", "StudyInstanceUID", "SeriesInstanceUID",
        "ImagePositionPatient", "ImageOrientationPatient", "PhotometricInterpretation",
        "PixelRepresentation", "PixelData"
    ]
    
    metadata = {}
    for key in metadata_keys:
        if hasattr(dicom_data, key):
            metadata[key] = getattr(dicom_data, key)
    return metadata

# Function to assess severity based on pixel intensity
def assess_severity(dicom_image, threshold):
    mean_intensity = np.mean(dicom_image)
    return "Severe Condition" if mean_intensity > threshold else "Non-Severe Condition"

# Function to prepare image for download
def get_image_bytes(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    return buf

# Set up the Streamlit app
st.title("Lumbar Spine DICOM Analysis App")

# Sidebar for user settings
st.sidebar.header("Settings")
threshold = st.sidebar.slider("Intensity Threshold for Severity", 50, 200, 100)

# Upload DICOM file
uploaded_file = st.file_uploader("Upload a DICOM file", type=["dcm"])

if uploaded_file:
    try:
        dicom_data = pydicom.dcmread(uploaded_file)
        dicom_image = dicom_data.pixel_array

        # Display Metadata
        st.subheader("Patient Details")
        metadata = display_metadata(dicom_data)
        for key, value in metadata.items():
            st.write(f"{key}: {value}")

        # Display DICOM Image with annotation
        st.subheader("DICOM Image with Annotation")
        severity = assess_severity(dicom_image, threshold)  # Get severity assessment

        fig, ax = plt.subplots()
        ax.imshow(dicom_image, cmap="gray")
        ax.axis("off")  # Hide axis

        # Add dynamic title and annotation to image
        annotation_text = f"Condition Severity: {severity}"
        ax.set_title(f"{metadata.get('SeriesDescription', 'DICOM Image')}\nMean: {np.mean(dicom_image):.2f}, Std: {np.std(dicom_image):.2f}", fontsize=10, color="white")

        # Draw a small circle or marker on a specific point (optional)
        ax.plot(dicom_image.shape[1] // 2, dicom_image.shape[0] // 2, 'o', color='white', markersize=8, markeredgecolor="black")

        st.pyplot(fig)

        # Display severity assessment below the image
        st.subheader("Severity Assessment")
        st.write(f"Condition Severity: {severity}")

        # Provide an option to download the processed image
        st.subheader("Download Processed Image")
        img_bytes = get_image_bytes(fig)
        st.download_button("Download Processed Image", img_bytes, "processed_image.png", "image/png")

    except Exception as e:
        st.error(f"Error reading DICOM file: {str(e)}")
