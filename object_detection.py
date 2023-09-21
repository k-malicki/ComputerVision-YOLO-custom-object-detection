import streamlit as st
from yolo_prediction import YOLO_Pred
from PIL import Image
import numpy as np

# Page config
st.set_page_config(page_title="Seed ",
                   layout="wide")

st.title("Witaj w aplikacji seed detector")
st.write("Aplikacja wykrywa ziarna znajdujące się na obrazach.")

# Main
with st.spinner("Proszę czekać."):
    yolo = YOLO_Pred(onnx_model="./model/best.onnx",
            data_yaml="./model/data.yaml")

# Upload image
def upload_image():
    file_uploader = st.file_uploader(label="Upload image")
    if file_uploader is not None:
        file_details = {
            "filename":file_uploader.name,
            "filetype":file_uploader.type,
            "filesize":file_uploader.size
        }

        if file_details["filetype"] in ("image/jpeg", "image/png"):
            st.success("Plik został poprawnie załadowany.")

            return {"file": file_uploader,
                    "details":file_details}
        
        else:
            st.error("Nieprawidłowy format pliku.")
            return None

def main():
    object = upload_image()

    if object:
        prediction = False
        img_obj = Image.open(object["file"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Podgląd pliku")
            st.image(img_obj)
        
        with col2:
            st.subheader("Szczegóły")
            st.write(object["details"])
            button = st.button("Analizuj")

            if button:
                st.spinner("Przetwarzanie")
                image_array = np.array(img_obj)
                pred_image = yolo.predictions(image_array)
                prediction_image = Image.fromarray(pred_image)
                prediction = True

        if prediction:
            st.subheader("Zdjęcie po analizie")
            st.image(prediction_image)


if __name__ == "__main__":
    main()