import streamlit as st
import cv2
import tempfile
from PIL import Image


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
output_path = 'test_data/tmp_thumbs/'

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
                # print(output_path + tmp_filename + "_frame" + str(count) + ".jpg")
                # cv2.putText(image, str(count/fps),(20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imwrite(output_path + tmp_filename + "_frame" + str(count) + ".jpg", image)     # save frame as JPEG file
                output_image = Image.open(output_path + tmp_filename + "_frame" + str(count) + ".jpg")
                st.image(output_image, caption='Thumbnail selected')
    else:
        st.text('No file selected')
