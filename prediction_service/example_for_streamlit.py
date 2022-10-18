import streamlit as st
from PIL import Image

#run this and you will get idea of what streamlit does (in bash terminal, after activate enviroment)
#run 'streamlit example_for_streamlit.py'

st.image(image, caption='sunrice from the mountain')


uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    bytes_date = uploaded_file.getvalue()
    image = image.open(uploaded_file)
    st.image(image, caption='sunrice from the mountain')

"""
# Deep Classifier Project

## workfolow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

if mlflow resorce not found error or to run mlflow follow below steps
    STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

    MLFLOW_TRACKING_URI=https://dagshub.com/c17hawke/FSDS_NOV_deepCNNClassifier.mlflow
    MLFLOW_TRACKING_USERNAME=c17hawke
    MLFLOW_TRACKING_PASSWORD=<> \
    (run above code one by one on bash terminal, before every commanda type 'export')

    STEP 2: install mlflow

    STEP 3: Set remote URI

    STEP 4: Use context manager of mlflow to start run and then log metrics, params and model
"""