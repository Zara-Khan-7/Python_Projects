import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import os
import io

# Set up output folder
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

st.title("🖼️ Image Processing App")
st.markdown("Upload an image, tweak the settings, and download your custom versions!")

uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    base_name = os.path.splitext(uploaded_file.name)[0]

    st.image(image, caption="Original Image", use_column_width=True)

    with st.sidebar:
        st.header("🎛️ Adjustments")
        brightness = st.slider("Brightness", 0.5, 3.0, 1.5)
        contrast = st.slider("Contrast", 0.5, 3.0, 1.8)
        apply_blur = st.checkbox("Apply Blur")
        convert_gray = st.checkbox("Convert to Grayscale")

    # Apply effects
    bright_image = ImageEnhance.Brightness(image).enhance(brightness)
    contrast_image = ImageEnhance.Contrast(bright_image).enhance(contrast)

    processed_image = contrast_image

    if apply_blur:
        processed_image = processed_image.filter(ImageFilter.BLUR)

    if convert_gray:
        processed_image = processed_image.convert("L")

    st.subheader("🖼️ Processed Image")
    st.image(processed_image, use_column_width=True)

    # Save processed image
    processed_path = os.path.join(output_folder, f"{base_name}_edited.png")
    processed_image.save(processed_path)

    # Prepare image for download
    img_byte_arr = io.BytesIO()
    processed_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    st.download_button(
        label="⬇️ Download Processed Image",
        data=img_byte_arr,
        file_name=f"{base_name}_edited.png",
        mime="image/png"
    )

    st.success(f"✅ Image saved to `{output_folder}` folder.")



# open the folder and run cmd and in cmd write streamlit run app.py