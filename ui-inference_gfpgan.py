import argparse
import cv2
import glob
import numpy as np
import os
import torch
from basicsr.utils import imwrite
import streamlit as st
from PIL import Image


from gfpgan import GFPGANer


class Args:
    pass

def enhance_image(input_img, args):
    # Set up background upsampler
    bg_upsampler = None
    if args.bg_upsampler == 'realesrgan':
        if not torch.cuda.is_available():
            st.warning('The unoptimized RealESRGAN is slow on CPU. Please use a GPU for better performance.')
        else:
            from basicsr.archs.rrdbnet_arch import RRDBNet
            from realesrgan import RealESRGANer
            model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
            bg_upsampler = RealESRGANer(
                scale=2,
                model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth',
                model=model,
                tile=args.bg_tile,
                tile_pad=10,
                pre_pad=0,
                half=True)

    # Set up GFPGAN restorer
    restorer = GFPGANer(
        model_path=args.model_path,
        upscale=args.upscale,
        arch=args.arch,
        channel_multiplier=args.channel_multiplier,
        bg_upsampler=bg_upsampler)

    # Restore image
    cropped_faces, restored_faces, restored_img = restorer.enhance(
        input_img,
        has_aligned=args.aligned,
        only_center_face=args.only_center_face,
        paste_back=True,
        weight=args.weight)

    return cropped_faces, restored_faces, restored_img

def main():
    st.set_page_config(page_title="Image Upscaler by ABDULKARIM", page_icon="🤖")
    st.header("Make Your Image Better + Face Enhancer")
    your_upload = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if your_upload is not None:
        input_img = Image.open(your_upload)
        input_img = np.array(input_img)

        st.image(input_img, caption="Uploaded Image", use_column_width=True)

        # User options in sidebar
        with st.sidebar:
            st.subheader("Options")
            upscale_factor = st.slider("Select Upscale Factor", min_value=2, max_value=4, step=1, value=2)
            weight = st.slider("Adjustable Weights", min_value=0.0, max_value=1.0, step=0.1, value=0.5)

        args = Args()
        args.upscale = upscale_factor
        args.bg_upsampler = 'realesrgan'
        args.bg_tile = 400
        args.version = '1.3'
        args.arch = 'clean'
        args.channel_multiplier = 2
        args.model_path = 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth'
        args.aligned = False
        args.only_center_face = False
        args.ext = 'auto'
        args.weight = weight

        # Process image
        cropped_faces, restored_faces, restored_img = enhance_image(input_img, args)

        # Display results
        st.subheader("Restored Faces")
        for idx, (cropped_face, restored_face) in enumerate(zip(cropped_faces, restored_faces)):
            st.image([cropped_face, restored_face], caption=[f"Cropped Face {idx + 1}", f"Restored Face {idx + 1}"], use_column_width=True)

        if restored_img is not None:
            st.subheader("Restored Image")
            st.image(restored_img, caption="Restored Image", use_column_width=True)

if __name__ == '__main__':
    main()