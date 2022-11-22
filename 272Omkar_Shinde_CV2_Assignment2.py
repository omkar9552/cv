import streamlit as st
import cv2
from PIL import Image
import numpy as np

def filter():
        wood = st.file_uploader("Upload Your Image For Filter", type=['jpg', 'png', 'jpeg'])
        salt = st.file_uploader("Upload Your Image To Remove salt and pepper", type=['jpg', 'png', 'jpeg'])
        if not wood or not salt:
               return None


        original_image_wood = Image.open(wood)
        original_image_wood = np.array(original_image_wood)

        st.image(original_image_wood, caption="★ Original Image of Wood★")

        st.text("______________________________________________________________________________________________")
        original_image_salt = Image.open(salt)
        original_image_salt = np.array(original_image_salt)

        st.image(original_image_salt, caption="★ Original Image of salt and pepper★")
        filter = st.radio(
                "➳ Choose your Favourite Filter 👇",
                ["twoconvkernel", "average_blurring", "guassian_blur", "median_blur","bilateral_blur","salt_pepper_removal"],
                key="filter"
            )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>',
             unsafe_allow_html=True)
        if filter == "twoconvkernel":
                twoconvkernel(original_image_wood)
        elif filter == "average_blurring":
                average_blurring(original_image_wood)
        elif filter == "guassian_blur":
                guassian_blur(original_image_wood)
        elif filter == "median_blur":
                median_blur(original_image_wood)
        elif filter == "salt_pepper_removal":
                salt_pepper_removal(original_image_salt)
        elif filter == "bilateral_blur":
                bilateral_blur(original_image_wood)       
        else:
                st.text("Sorry Filter is not Available")

        
def twoconvkernel(original_image_wood):
    kernel2 = np.ones((5, 5), np.float32) / 25
    img = cv2.filter2D(src=original_image_wood, ddepth=-1, kernel=kernel2)
    label = "✵ output image✵" 
    st.image(img, caption=label)

def average_blurring(original_image_wood):
    img_blur = cv2.blur(src=original_image_wood, ksize=(3,3)) # Using the blur function to blur an image where ksize is the kernel size
    label = "✵ output image✵" 
    st.image(img_blur, caption=label)
    
def guassian_blur(original_image_wood):
    gau_blur = cv2.GaussianBlur(src=original_image_wood, ksize=(5,5),sigmaX=0, sigmaY=0)
    label = "✵ output image✵" 
    st.image(gau_blur, caption=label)

def median_blur(original_image_wood):
    median = cv2.medianBlur(src=original_image_wood, ksize=5)
    label = "✵ output image✵" 
    st.image(median, caption=label)

def salt_pepper_removal(original_image_salt):
    median = cv2.medianBlur(src=original_image_salt, ksize=3)
    label = "✵ output image✵" 
    st.image(median, caption=label)

def bilateral_blur(original_image_wood):
    bilateral_filter = cv2.bilateralFilter(src=original_image_wood, d=9, sigmaColor=75, sigmaSpace=75)
    label = "✵ output image✵" 
    st.image(bilateral_filter, caption=label)
    
def main_opration():
    st.title("Blurring and salt pepper noise removal")
   

    filter()
    st.text("_____________________________________________________________________________________________________________")

if __name__ == "__main__":
    main_opration()
    
