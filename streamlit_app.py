import streamlit as st
import cv2
import tempfile
from PIL import Image

st.set_page_config(layout="wide")
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

col1, col2 = st.columns(2)

with col1:
    f = st.file_uploader("Upload file")
    if f != None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(f.read())
        video_file = open(tfile.name, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
with col2:
    if f != None:
        vidcap = cv2.VideoCapture(tfile.name)
        tmp_filename = tfile.name.split('/')[-1]
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        count = 0
        success = True
        # font = cv2.FONT_HERSHEY_PLAIN

        while success:
            success,image = vidcap.read()
            count+=1
            # print("time stamp current frame:",count/fps)
            if count/fps == 3:
                cv2.imwrite(tmp_filename + "_frame" + str(count) + ".jpg", image)     # save frame as JPEG file
                output_image = Image.open(tmp_filename + "_frame" + str(count) + ".jpg")
                st.image(output_image, caption='Thumbnail selected')
    else:
        st.text('No file selected')
