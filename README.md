# Make Your Image Better + Face Enhancer
# (GFPGAN - webui) Image Upscaler & Face Restoration

### How to install
> it is so easy; just download/clone the repository and RUN
```bash
git clone https://github.com/abdulkarim1422/GFPGAN-webui
```
- after downloading to your PC, run the file name `INSTALL REQUIREMENTS.cmd` and wait (you need to have python installed)
- now you must be ready to use, you can run `WEBUI RUN.cmd` to use the user interface version, or run `AUTO RUN.cmd` to use the auto version

# WEBUI Version
- run `WEBUI RUN.cmd`
- easy to use, just upload your photo

![image](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/208af0e4-cf1f-4a9c-808f-2fd68e073b21)


| original image | upscaled image | faces one by one |
| :--- | :--- | :--- |
| ![image](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/b1606778-9cc7-409f-ac64-89212733f9e3) | ![image_2023-12-04_00-21-33](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/0050c5bc-95c0-4364-b7d4-eaa2246c13fd) | ![image_2023-12-04_00-21-59](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/b6ecc94d-3006-45fa-b5aa-b6a9d1c04c0f) |

# AUTO Version
- also easy to use; first place your image/images in the `inputs` folder
- now run `AUTO RUN.cmd`; and wait
- results will take place in the `results` folder

| `inputs` folder | `results` folder |
| :- | :- |
| ![image](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/77f1f078-dcff-438a-9a4d-08c87911a1aa) | ![image](https://github.com/abdulkarim1422/GFPGAN-webui/assets/54938173/6bb85ae3-cfce-4a3b-b066-e3a86cc6561b) |



### REQUIREMENTS / TESTED ON
- I tested this model on PC running Windows 11
- Python 3.10.11
- torch 2.1.0+cpu
- torch 2.1.0+cu118

### Recources / References
- [@TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN)
- [streamlit](https://github.com/streamlit/streamlit)
