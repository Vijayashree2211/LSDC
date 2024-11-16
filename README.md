Overview
The Lumbar Spine Degenerative Classification (LSDC) project aims to classify lumbar spine MRI images as severe or not severe. Using convolutional neural networks (CNNs), this system analyzes DICOM images to provide accurate and actionable insights into lumbar spine degenerative conditions.
Dataset : https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification/data
Features
DICOM Image Processing: Supports viewing and processing DICOM images.
Classification: Determines whether an image is classified as "Severe" or "Not Severe."
Streamlit Application: User-friendly interface for viewing images and classification results.
Metadata Display: Shows relevant metadata (e.g., patient age, study description) when available.
Project Structure
graphql
Copy code
lsdc/
├── data/                 # DICOM images and datasets
├── models/               # Trained models (e.g., lumbar_spine_model.h5)
├── notebooks/            # Jupyter notebooks for data exploration and model development
├── src/                  # Source code
│   ├── preprocessing/    # Preprocessing scripts for DICOM and image data
│   ├── models/           # CNN model implementation and training scripts
│   └── utils/            # Helper functions (e.g., DICOM metadata extraction)
├── streamlit_app/        # Streamlit application files
├── results/              # Classification results and evaluation metrics
├── docs/                 # Documentation
├── README.md             # Project overview
├── requirements.txt      # Python dependencies
└── LICENSE               # Project license
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/lsdc.git
cd lsdc
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run streamlit_app/app.py

Methodology

Data Preparation:
DICOM images were preprocessed to ensure compatibility with the CNN model.
Metadata was extracted to provide additional context.

Model Training:
A CNN model was developed and trained using annotated MRI datasets.

Application Development:

A Streamlit application was created to provide a user-friendly interface for classification and image analysis.
Usage
Upload a DICOM image using the Streamlit interface.
View the image and its metadata.
Check the classification result ("Severe" or "Not Severe").
Results
Achieved 90%+ accuracy on the test dataset.
Real-time classification through the Streamlit application.

