# 🧠 Python Projects Collection – By Zara Khan

Welcome to my Python Projects Repo! 🚀  
This collection includes beginner-to-intermediate level projects I’ve built during class assignments, all designed to improve logical thinking, problem-solving, and real-world application skills.

---

## 📦 Projects Included

### 1️⃣ 🔐 Password Generator
A secure password generator that creates strong, random passwords using letters, numbers, and special characters.

**🛠 Features:**
- Customizable password length
- Includes upper/lowercase, digits, symbols
- Easy to use and terminal-based

---

### 2️⃣ 📊 Report Card Generator
Generates a student's report card based on entered marks for each subject.

**📌 Features:**
- Accepts multiple subjects
- Calculates total, average, and grade
- Neat and readable output

---

### 3️⃣ 🔁 Unit Converter
Convert units such as:
- Length (meters ↔ kilometers)
- Temperature (Celsius ↔ Fahrenheit)
- Weight (grams ↔ kilograms)

**🔧 Features:**
- Menu-based options
- Simple `if-elif` logic
- Accurate calculations

---

### 4️⃣ 📚 Library Manager
A mini system to manage book borrowing and returns in a library.

**📘 Features:**
- Add/remove books
- Lend books to users
- Keep track of borrowed books
- CLI-based interaction

---

### 5️⃣ 💡 Growth Mindset App
A motivational Streamlit web app to encourage positive thinking.

**🌟 Features:**
- Shows daily affirmations or quotes
- Clean and colorful UI
- Streamlit-based with interactive elements

---

### 6️⃣ 💎 Diamond Pattern Generator
A fun project that prints a centered diamond using `*` characters.

**📐 Output Example (size = 5):**
*

---

### 7️⃣ 🧩 Deductive Logic Game
A simple Python guessing game that encourages critical thinking and deduction.

**🎯 Features:**
- Guess the correct number or pattern
- Tracks attempts and gives feedback
- Good for practicing logic and loops

---

## 🛠 How to Run Any Project

1. **Clone the Repository:**
```bash
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects


You said:
C:\Python\growth_mindset>pip install streamlit
Fatal error in launcher: Unable to create process using '"C:\Python312\python.exe"  "C:\Python312\Scripts\pip.exe" install streamlit': The system cannot find the file specified.


ChatGPT said:
This error typically means that your Python or pip installation is not properly configured, or the launcher can't find the necessary files. Here’s how to fix it:

✅ Step-by-step Fix
1. Check if Python is installed correctly
Run this in Command Prompt:

bash
Copy
Edit
python --version
If it throws an error, Python is not correctly installed or not added to the system PATH.

2. Reinstall or Repair Python
Go to https://www.python.org/downloads/ and download the latest version.

During installation, check the box that says "Add Python to PATH".

Choose "Repair" if already installed, or reinstall fresh.

🔁 Alternative: Use python -m pip
Sometimes pip doesn’t work on its own, but this does:

bash
Copy
Edit
python -m pip install streamlit
🧹 Check and Fix Environment Variables
If you already have Python installed:

Press Windows + R, type sysdm.cpl, hit Enter.

Go to the Advanced tab > Environment Variables.

Under "System variables", find Path and click Edit.

Ensure you have paths like these (adjust depending on where Python is installed):

makefile
Copy
Edit
C:\Python312\
C:\Python312\Scripts\
🧪 Final Test
After setting things up, run:

bash
Copy
Edit
python -m pip install streamlit
Then:

bash
Copy
Edit
streamlit hello
Let me know what happens or if you want help verifying your Python install.






You said:
python --version this shows me the version  


ChatGPT said:
Awesome — that means Python is installed and at least partially working ✅

Now let’s try installing Streamlit using the more reliable method:

🚀 Run this in Command Prompt:
bash
Copy
Edit
python -m pip install streamlit
This tells Python to run pip directly and usually avoids the launcher error you saw earlier.

Let me know what output you get — or if it still complains, I can walk you through checking your pip setup.






You said:
pip setup 


ChatGPT said:
Great! Let’s make sure pip is properly set up.

✅ Step-by-Step: Check if pip is Working
1. Check pip version
Run this in Command Prompt:

bash
Copy
Edit
python -m pip --version
If it shows something like:

vbnet
Copy
Edit
pip 24.0 from C:\Python312\Lib\site-packages\pip (python 3.12)
Then pip is installed correctly.

🔄 If pip is NOT found:
You can reinstall it using this command:

bash
Copy
Edit
python -m ensurepip --upgrade
Then test again with:

bash
Copy
Edit
python -m pip --version
🔧 If that still doesn't work…
You can manually reinstall pip:

Download get-pip.py.

Open Command Prompt where the file is downloaded.

Run:

bash
Copy
Edit
python get-pip.py
This will install the latest version of pip.

📦 After pip is working
Finally, install Streamlit:

bash
Copy
Edit
python -m pip install streamlit
Let me know where you're stuck or what message you get after trying any of the steps — I’ll guide you from there.






You said:
pip shows in cmd


ChatGPT said:
Perfect — if pip shows in the command prompt, that means it's installed and ready to go! 🎉

Now, you can install Streamlit using:

bash
Copy
Edit
pip install streamlit
Or, if you prefer the safer route:

bash
Copy
Edit
python -m pip install streamlit
Once it's installed, test it by running:

bash
Copy
Edit
streamlit hello
That should launch a sample Streamlit app in your browser.

Let me know how it goes or if anything unexpected pops up!






You said:

C:\Project-04-Assignments>git clone https://github.com/HadiqaGohar/Project-4-Assignments.git
Cloning into 'Project-4-Assignments'...
remote: Enumerating objects: 900, done.
remote: Counting objects: 100% (131/131), done.
remote: Compressing objects: 100% (123/123), done.
remote: Total 900 (delta 55), reused 0 (delta 0), pack-reused 769 (from 2)
Receiving objects: 100% (900/900), 1.50 MiB | 1.95 MiB/s, done.
Resolving deltas: 100% (325/325), done.
error: invalid path 'Assignments 1 to 6/Project 1: Mad libs Python Project/README.md'
fatal: unable to checkout working tree
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore --source=HEAD :/'


ChatGPT said:
Ah, classic Windows issue! 😅
This error happens because Windows doesn't support colons : in file or folder names, and Git is trying to create this path:

css
Copy
Edit
Assignments 1 to 6/Project 1: Mad libs Python Project/README.md
The colon : in Project 1: Mad libs... is the problem.

🛠️ Fix Options
✅ Option 1: Clone with Filename Conversion (Safe way)
Use this to auto-convert incompatible characters (works best on Windows):

bash
Copy
Edit
git config --global core.protectNTFS false
git clone https://github.com/HadiqaGohar/Project-4-Assignments.git
Sometimes just disabling NTFS protection helps bypass the error.

✅ Option 2: Clone without checking out
This lets you clone the repo without pulling files to the file system (so you can rename things manually):

bash
Copy
Edit
git clone --no-checkout https://github.com/HadiqaGohar/Project-4-Assignments.git
cd Project-4-Assignments
git sparse-checkout init --cone
git sparse-checkout set "Assignments 1 to 6"
Then manually rename the offending folder using:

bash
Copy
Edit
git mv "Assignments 1 to 6/Project 1: Mad libs Python Project" "Assignments 1 to 6/Project 1 - Mad libs Python Project"
And finally:

bash
Copy
Edit
git checkout
🧼 Option 3: Clone on WSL or Linux/Mac (if you have WSL)
If you have WSL (Windows Subsystem for Linux), this error won’t happen. You can open Ubuntu or Debian from the Start Menu and run:

bash
Copy
Edit
git clone https://github.com/HadiqaGohar/Project-4-Assignments.git
Then work with it safely from there.

Let me know if you'd like to go with Option 1, 2, or need help setting up WSL — I got you!






You said:
1


ChatGPT said:
Nice — let’s go with Option 1 then. Here’s exactly what to do:

✅ Step-by-step Fix (Disable NTFS protection)
Open Command Prompt (as administrator just to be safe).

Run this command:

bash
Copy
Edit
git config --global core.protectNTFS false
Then try cloning again:

bash
Copy
Edit
git clone https://github.com/HadiqaGohar/Project-4-Assignments.git
🎯 What this does
It tells Git to stop blocking files that may cause issues on Windows NTFS (like names with :), which helps bypass this specific checkout failure.

Let me know if the cloning works after that — or if you still hit errors, I’ll help you clean it up!






You said:
it dosent works


ChatGPT said:
No worries — let’s go with a guaranteed method to make it work 💪
Since Option 1 didn’t work, we’ll try the safe and reliable workaround using --no-checkout so you can rename the offending folder.

✅ Try this (No checkout, then rename)
Run the following commands step by step in your Command Prompt:

bash
Copy
Edit
git clone --no-checkout https://github.com/HadiqaGohar/Project-4-Assignments.git
cd Project-4-Assignments
Now rename the problematic folder before checkout:

bash
Copy
Edit
git config core.protectNTFS false
git sparse-checkout init --cone
git sparse-checkout set "Assignments 1 to 6"
Then rename the folder with a safe name (replacing the colon):

bash
Copy
Edit
git mv "Assignments 1 to 6/Project 1: Mad libs Python Project" "Assignments 1 to 6/Project 1 - Mad libs Python Project"
Finally, try checking out the files:

bash
Copy
Edit
git checkout
💡 If git mv gives an error
You can manually rename the folder in the .git/index or check out only specific folders instead.

Let me know how far you get or if you want me to walk you through doing it even easier using GitHub's website (e.g., downloading a ZIP instead).






You said:
how to start streamlit


ChatGPT said:
Nice! Once Streamlit is installed, starting it is super simple 🚀

✅ To Start Streamlit:
Open Command Prompt

Navigate to your project folder (if you have a .py file with Streamlit code):

bash
Copy
Edit
cd path\to\your\project
Run this command:

bash
Copy
Edit
streamlit run your_script_name.py
Replace your_script_name.py with the name of your Python file.

🧪 Example
If your file is named app.py, you'd run:

bash
Copy
Edit
streamlit run app.py
Then it will open your default web browser with a local URL like:

arduino
Copy
Edit
http://localhost:8501
🧠 Pro Tip
If you just want to test Streamlit, create a file called demo.py and paste this in:

python
Copy
Edit
import streamlit as st

st.title("🚀 Hello Streamlit!")
st.write("This is a test app.")
Then run:

bash
Copy
Edit
streamlit run demo.py
Let me know if you want help writing your first Streamlit app or troubleshooting anything!






You said:


import os
from PIL import Image, ImageEnhance, ImageFilter

# Ask the user to input the path to the image file
image_path = input("Please enter the path to your image file: ").strip()

# Load the image
image = Image.open(image_path)

# Get the base name (file name without extension)
base_name = os.path.splitext(os.path.basename(image_path))[0]

# Create a folder for saving images if it doesn't exist
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

# Convert to grayscale
gray_image = image.convert("L")

# Apply blur filter
blurred_image = image.filter(ImageFilter.BLUR)

# Adjust brightness (1.5 times brighter)
brightness_enhancer = ImageEnhance.Brightness(image)
bright_image = brightness_enhancer.enhance(1.5)

# Adjust contrast (1.8 times higher contrast)
contrast_enhancer = ImageEnhance.Contrast(image)
contrast_image = contrast_enhancer.enhance(1.8)

# Save the edited images with the base name
gray_image.save(os.path.join(output_folder, f"{base_name}_gray.jpg"))
blurred_image.save(os.path.join(output_folder, f"{base_name}_blur.jpg"))
bright_image.save(os.path.join(output_folder, f"{base_name}_bright.jpg"))
contrast_image.save(os.path.join(output_folder, f"{base_name}_contrast.jpg"))

# Show all the images
image.show(title="Original Image")
gray_image.show(title="Grayscale Image")
blurred_image.show(title="Blurred Image")
bright_image.show(title="Brighter Image")
contrast_image.show(title="High Contrast Image")

print(f"✅ Image processing complete! Check your 'generated_images' folder for the new images.")


ChatGPT said:
Nice script! 🔥 You’ve created a mini image processing pipeline using Pillow that:

Converts to grayscale

Applies blur

Increases brightness

Boosts contrast

Saves all edited images into a folder

Want to turn it into a Streamlit app?
You can make this interactive with file upload, sliders for brightness/contrast, and image previews — all in the browser.

Here’s a Streamlit version of your script:

🖼️ Streamlit Version
Save this as app.py:

python
Copy
Edit
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import os

st.title("🖼️ Image Processing App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    st.write("### Choose Enhancements:")

    # Sliders
    brightness = st.slider("Brightness", 0.5, 3.0, 1.5)
    contrast = st.slider("Contrast", 0.5, 3.0, 1.8)

    # Apply filters
    gray_image = image.convert("L")
    blurred_image = image.filter(ImageFilter.BLUR)
    bright_image = ImageEnhance.Brightness(image).enhance(brightness)
    contrast_image = ImageEnhance.Contrast(image).enhance(contrast)

    st.write("### Processed Images")

    st.image(gray_image, caption="Grayscale", use_column_width=True)
    st.image(blurred_image, caption="Blurred", use_column_width=True)
    st.image(bright_image, caption=f"Brightness x{brightness}", use_column_width=True)
    st.image(contrast_image, caption=f"Contrast x{contrast}", use_column_width=True)
▶️ To Run It:
Save the code above as app.py

In the same folder, open Command Prompt and run:

bash
Copy
Edit
streamlit run app.py
Upload an image from the browser and enjoy!

Let me know if you want to add:

Download buttons

More filters

Sidebar controls

Auto-saving to a folder

Happy coding! 🧑‍💻✨






You said:
add all these


ChatGPT said:
Yesss! Let's go all in 💥
Here's your upgraded Streamlit image editor app with:

✅ File upload
✅ Brightness & contrast sliders
✅ Blur toggle
✅ Grayscale toggle
✅ Auto-save to generated_images/
✅ Download buttons for each version
✅ Sidebar for controls

🔥 Full Upgraded Code (app.py)
python
Copy
Edit
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

▶️ How to Run:
Save this code in app.py

In the same folder, run:

bash
Copy
Edit
streamlit run app.py
Upload an image → Adjust → View → Download 🎯

Want more advanced filters? Cropping? Watermarking? Fancy UI themes? Let me know — we can level this up even more 🔥






You said:
create a read me file for unit convertor app using python with my git link https://github.com/Zara-Khan-7/Python_Projects.git


ChatGPT said:
Sure! Here's a clean and professional README.md file tailored for your Unit Converter App built with Python, and linking to your GitHub repo:

📄 README.md
markdown
Copy
Edit
# 🧮 Unit Converter App (Python)

Welcome to the **Unit Converter App** — a simple and user-friendly Python application that allows users to convert values between different units of measurement including length, temperature, weight, and more.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Open Source](https://img.shields.io/badge/License-MIT-brightgreen)

## 🔗 Repository

Check it out on GitHub:  
👉 [https://github.com/Zara-Khan-7/Python_Projects](https://github.com/Zara-Khan-7/Python_Projects)

---

## ✨ Features

- Convert between various unit types:
  - Length (meters, kilometers, miles, etc.)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Weight (grams, kilograms, pounds, etc.)
- Interactive user input
- Clean terminal-based UI
- Easy to extend with more units

---

## 🚀 How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects/Unit_Converter
Run the App

bash
Copy
Edit
python unit_converter.py
🛠️ Requirements
Python 3.x (no external libraries required)

📂 Project Structure
markdown
Copy
Edit
Python_Projects/
│
└── Unit_Converter/
    ├── unit_converter.py
    └── README.md
💡 Future Improvements
Add GUI using Tkinter or Streamlit

Add currency converter

Add support for live exchange rates via API

Dark mode UI (if GUI is added)

📬 Contact
For suggestions or feedback, feel free to reach out via GitHub Issues or submit a pull request.

📄 License
This project is licensed under the MIT License.

Made with ❤️ by Zara Khan

vbnet
Copy
Edit

---

Let me know if:
- The filename is different (I'll update the path)
- You want a GUI version mentioned
- You want a badge for "Streamlit App" if you're planning to convert it to a web version

Want me to drop this directly into a `README.md` file too?





You said:
yes


ChatGPT said:
All done! ✅ Your README.md file is ready and you can download it here.

You can now drop this file into your Unit_Converter folder on GitHub or your local project directory.

Want me to help create the unit_converter.py file too if you haven’t written it yet? ​​






You said:
create it as a whole so that i copy all at once


ChatGPT said:
Got it! Here's the full content for both README.md and a simple unit_converter.py file in one go. You can copy everything below and paste it directly into your project.

📝 Full Project Files
1. unit_converter.py - Your Python App
python
Copy
Edit
def convert_length():
    print("\nLength Conversion")
    length = float(input("Enter length: "))
    from_unit = input("Convert from (meters, kilometers, miles): ").strip().lower()
    to_unit = input("Convert to (meters, kilometers, miles): ").strip().lower()
    
    # Conversion logic
    conversion_factors = {
        ('meters', 'kilometers'): 0.001,
        ('meters', 'miles'): 0.000621371,
        ('kilometers', 'meters'): 1000,
        ('kilometers', 'miles'): 0.621371,
        ('miles', 'meters'): 1609.34,
        ('miles', 'kilometers'): 1.60934
    }

    if from_unit == to_unit:
        print(f"{length} {from_unit} is already the same in {to_unit}.")
    elif (from_unit, to_unit) in conversion_factors:
        converted_value = length * conversion_factors[(from_unit, to_unit)]
        print(f"{length} {from_unit} = {converted_value} {to_unit}")
    else:
        print("Invalid unit conversion.")
    
def convert_temperature():
    print("\nTemperature Conversion")
    temperature = float(input("Enter temperature: "))
    from_unit = input("Convert from (celsius, fahrenheit, kelvin): ").strip().lower()
    to_unit = input("Convert to (celsius, fahrenheit, kelvin): ").strip().lower()

    # Conversion logic
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            result = (temperature * 9/5) + 32
        elif to_unit == "kelvin":
            result = temperature + 273.15
        else:
            result = temperature
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            result = (temperature - 32) * 5/9
        elif to_unit == "kelvin":
            result = (temperature - 32) * 5/9 + 273.15
        else:
            result = temperature
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            result = temperature - 273.15
        elif to_unit == "fahrenheit":
            result = (temperature - 273.15) * 9/5 + 32
        else:
            result = temperature
    else:
        print("Invalid unit.")
        return

    print(f"{temperature} {from_unit} = {result} {to_unit}")

def convert_weight():
    print("\nWeight Conversion")
    weight = float(input("Enter weight: "))
    from_unit = input("Convert from (grams, kilograms, pounds): ").strip().lower()
    to_unit = input("Convert to (grams, kilograms, pounds): ").strip().lower()

    # Conversion logic
    conversion_factors = {
        ('grams', 'kilograms'): 0.001,
        ('grams', 'pounds'): 0.00220462,
        ('kilograms', 'grams'): 1000,
        ('kilograms', 'pounds'): 2.20462,
        ('pounds', 'grams'): 453.592,
        ('pounds', 'kilograms'): 0.453592
    }

    if from_unit == to_unit:
        print(f"{weight} {from_unit} is already the same in {to_unit}.")
    elif (from_unit, to_unit) in conversion_factors:
        converted_value = weight * conversion_factors[(from_unit, to_unit)]
        print(f"{weight} {from_unit} = {converted_value} {to_unit}")
    else:
        print("Invalid unit conversion.")
    
def main():
    while True:
        print("\nWelcome to Unit Converter!")
        print("1. Length Conversion")
        print("2. Temperature Conversion")
        print("3. Weight Conversion")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()

        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_temperature()
        elif choice == '3':
            convert_weight()
        elif choice == '4':
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
2. README.md - Your README File
markdown
Copy
Edit
# 🧮 Unit Converter App (Python)

Welcome to the **Unit Converter App** — a simple and user-friendly Python application that allows users to convert values between different units of measurement including length, temperature, weight, and more.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Open Source](https://img.shields.io/badge/License-MIT-brightgreen)

## 🔗 Repository

Check it out on GitHub:  
👉 [https://github.com/Zara-Khan-7/Python_Projects](https://github.com/Zara-Khan-7/Python_Projects)

---

## ✨ Features

- Convert between various unit types:
  - Length (meters, kilometers, miles, etc.)
  - Temperature (Celsius, Fahrenheit, Kelvin)
  - Weight (grams, kilograms, pounds, etc.)
- Interactive user input
- Clean terminal-based UI
- Easy to extend with more units

---

## 🚀 How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects/Unit_Converter
Run the App

bash
Copy
Edit
python unit_converter.py
🛠️ Requirements
Python 3.x (no external libraries required)

📂 Project Structure
markdown
Copy
Edit
Python_Projects/
│
└── Unit_Converter/
    ├── unit_converter.py
    └── README.md
💡 Future Improvements
Add GUI using Tkinter or Streamlit

Add currency converter

Add support for live exchange rates via API

Dark mode UI (if GUI is added)

📬 Contact
For suggestions or feedback, feel free to reach out via GitHub Issues or submit a pull request.

📄 License
This project is licensed under the MIT License.

Made with ❤️ by Zara Khan

yaml
Copy
Edit

---

### 🚀 What to Do Next:

1. Copy **both** the `unit_converter.py` and `README.md` content into your project.
2. For `unit_converter.py`, save it in your project directory.
3. For `README.md`, save it in the root of your project folder.

You’re all set! 🎉 Let me know if you need any more help with this.

2/2






You said:
create a readme file for report card using python


ChatGPT said:
Sure! Here's a well-structured README.md file for your Report Card App using Python — suitable for school projects, portfolio showcases, or GitHub repositories.

📄 README.md — Report Card App (Python)
markdown
Copy
Edit
# 📝 Report Card App (Python)

This is a simple **Report Card Generator** built using Python. It allows users to input a student's name, roll number, subjects, and marks, then automatically calculates the total, average, and grade.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## ✨ Features

- Enter student details (name, roll number, etc.)
- Add subjects and corresponding marks
- Automatically calculate:
  - Total Marks
  - Percentage
  - Grade based on performance
- Display results in a clear format

---

## 🛠️ Technologies Used

- Python 3.x
- No external libraries needed

---

## 🚀 How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects/Report_Card
Run the App

bash
Copy
Edit
python report_card.py
🧮 Grading Logic
You can customize this logic in the script. Here's an example:

Percentage	Grade
90 – 100%	A+
80 – 89%	A
70 – 79%	B
60 – 69%	C
50 – 59%	D
Below 50%	F
📂 Project Structure
markdown
Copy
Edit
Python_Projects/
│
└── Report_Card/
    ├── report_card.py
    └── README.md
💡 Future Ideas
Export the report card to a PDF or CSV file

GUI version using Tkinter

Support multiple students and store results in a database

Send report card via email

📬 Contact
Have suggestions or improvements?
Create an issue or submit a pull request at
👉 https://github.com/Zara-Khan-7/Python_Projects

📄 License
Licensed under the MIT License.

Created with 💙 by Zara Khan

yaml
Copy
Edit

---

Let me know if you'd like me to create the actual `report_card.py` script too or customize it based on your current code!





You said:
# Footer
st.markdown('<div class="footer">Made by Moiz Ahmed Shaikh</div>', unsafe_allow_html=True) replace with my name and change some design also


ChatGPT said:
Sure! Here's an updated and improved version of your Streamlit footer, with your name and a bit of enhanced design using inline CSS for better style:

✅ Updated Footer
python
Copy
Edit
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: white;
            background-color: #0e1117;
            padding: 10px;
            font-size: 16px;
            border-top: 1px solid #444;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.3);
        }
    </style>
    <div class="footer">
        Made with ❤️ by <strong>Zara Khan</strong>
    </div>
    """,
    unsafe_allow_html=True
)
💡 What's Changed:
✅ Your name is now Zara Khan

🎨 Improved color scheme (dark background, white text)

✨ Added subtle border and shadow for better visibility

📱 Fixed position at the bottom of the screen

Let me know if you’d like it to auto-hide, be sticky only when scrolling, or include social icons!






You said:
create readme for this


ChatGPT said:
Absolutely! Here's a polished and stylish README.md file for your Streamlit-based project that includes a custom footer and credits you as the creator.

📄 README.md — Streamlit App with Custom Footer
markdown
Copy
Edit
# ⚡ Streamlit App with Custom Footer

This is a **Streamlit-powered Python app** featuring a beautiful custom footer made with HTML and CSS. It’s perfect for personal projects, portfolios, or showcasing your Python skills with a professional touch.

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🎨 Features

- Clean, fixed-position footer at the bottom of the screen
- Customizable HTML & CSS styling
- Responsive and minimal design
- Displays author credit in a stylish way

---

## 🧑‍💻 Author Credit Footer Code

```python
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: white;
            background-color: #0e1117;
            padding: 10px;
            font-size: 16px;
            border-top: 1px solid #444;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.3);
        }
    </style>
    <div class="footer">
        Made with ❤️ by <strong>Zara Khan</strong>
    </div>
    """,
    unsafe_allow_html=True
)
🚀 How to Run This App
Install Streamlit (if not already installed):

bash
Copy
Edit
pip install streamlit
Run the App:

bash
Copy
Edit
streamlit run your_script.py
Replace your_script.py with the name of your Python file.

💡 Use Cases
Add a professional touch to your Streamlit dashboards

Show personal branding or contact info

Credit yourself in portfolio projects

🔗 Related Links
Streamlit Docs: https://docs.streamlit.io

My GitHub: https://github.com/Zara-Khan-7

📄 License
This project is licensed under the MIT License.






You said:
"""
Write a Python program to draw a diamond of "*" using loops and string repetition.
"""

def diamond_pattern():
    num = 5
    for i in range(1, num+1):
        print(" " * (num - i) + "*" * (2 * i-1))

    for i in range(num-1, 0, -1):
        print(" " * (num - i) + "*" * (2 * i-1))

diamond_pattern


ChatGPT said:
You're almost there! The logic is correct, but you're missing the parentheses when calling the function at the end. Here's the corrected and slightly polished version of your Python program to draw a diamond pattern using *:

✅ Final Version
python
Copy
Edit
"""
Write a Python program to draw a diamond of "*" using loops and string repetition.
"""

def diamond_pattern():
    num = 5  # You can change this number to make a bigger or smaller diamond

    # Upper half
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))

    # Lower half
    for i in range(num - 1, 0, -1):
        print(" " * (num - i) + "*" * (2 * i - 1))

# Function call
diamond_pattern()
🧪 Sample Output (for num = 5):
markdown
Copy
Edit
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
Let me know if you'd like to make this a CLI tool or use input() so users can enter their own size!






You said:
readme for this


ChatGPT said:
Of course! Here's a clean and beginner-friendly README.md file for your Diamond Pattern Generator in Python:

📄 README.md — Diamond Pattern Generator (Python)
markdown
Copy
Edit
# 💎 Diamond Pattern Generator in Python

This is a simple Python program that prints a **diamond pattern** made of asterisks (`*`) using loops and string multiplication. It's great for learning nested loops and basic string operations in Python.

---

## 🧠 What It Does

- Takes a fixed height (can be changed)
- Prints a centered diamond shape using `*`
- Uses `for` loops and string repetition (`*` operator)

---

## 📌 Example Output (for height = 5)

markdown
Copy
Edit
*
markdown
Copy
Edit
*
yaml
Copy
Edit

---

## 🧾 Code Overview

```python
def diamond_pattern():
    num = 5  # Change this value to increase/decrease the size of the diamond

    # Upper half of the diamond
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))

    # Lower half of the diamond
    for i in range(num - 1, 0, -1):
        print(" " * (num - i) + "*" * (2 * i - 1))

# Run the function
diamond_pattern()
🚀 How to Run
Clone the repo or copy the code

Make sure Python is installed

Save the code in a .py file, for example: diamond.py

Run the script:

bash
Copy
Edit
python diamond.py
📂 Project Structure
Copy
Edit
Diamond_Pattern/
├── diamond.py
└── README.md
💡 Tips
You can make the diamond taller or shorter by changing num

Try using input() to let users set the size dynamically

📄 License
This project is open-source and free to use under the MIT License.

Created with 💻 by Zara Khan

yaml
Copy
Edit

---

Let me know if you'd like to turn this into a GUI or web-based pattern generator using Streamlit or Tkinter!





You said:
create a readme file that includes all the above class assignment details


ChatGPT said:
Here’s a complete README.md file that includes all your class assignment details — the Unit Converter, Report Card App, Diamond Pattern, and the Streamlit App with a Custom Footer — bundled into one polished markdown document for your GitHub repo.

📄 README.md — Python Class Assignments Collection
markdown
Copy
Edit
# 🐍 Python Projects – Class Assignments by Zara Khan

Welcome to my collection of Python-based class assignments! These mini projects and apps demonstrate fundamental programming concepts using loops, conditionals, functions, and simple UI with Streamlit. Perfect for beginners and those looking to build a solid Python foundation.

---

## 📁 Projects Included

### 1️⃣ Unit Converter App (Python)
A simple Python app that converts units such as:
- Length (meters ↔ kilometers)
- Temperature (Celsius ↔ Fahrenheit)
- Weight (grams ↔ kilograms)

📌 **Features:**
- Clean input/output using the terminal
- Uses `if-elif` statements for logic
- Beginner-friendly structure

🔗 [View Code](https://github.com/Zara-Khan-7/Python_Projects/tree/main/Unit_Converter)

---

### 2️⃣ Report Card Generator
Generates a student's report card based on input marks, calculates total, percentage, and assigns grades.

📌 **Features:**
- Input: Name, Roll No, Subject Marks
- Output: Total, Average, Grade
- Customizable grading logic

📊 **Sample Grade Logic:**
| Percentage      | Grade |
|-----------------|-------|
| 90 – 100%       | A+    |
| 80 – 89%        | A     |
| 70 – 79%        | B     |
| 60 – 69%        | C     |
| 50 – 59%        | D     |
| Below 50%       | F     |

🔗 [View Code](https://github.com/Zara-Khan-7/Python_Projects/tree/main/Report_Card)

---

### 3️⃣ Diamond Pattern Generator

A small program that draws a diamond using `*` characters based on a fixed size using nested loops.

📌 **Features:**
- Clean diamond shape made of asterisks
- Great for learning string repetition and loop nesting

🔍 **Output Example:**
markdown
Copy
Edit
*
markdown
Copy
Edit
*
php-template
Copy
Edit

🔗 [View Code](https://github.com/Zara-Khan-7/Python_Projects/tree/main/Diamond_Pattern)

---

### 4️⃣ Streamlit App with Custom Footer

A basic Streamlit web app that includes a **custom-designed footer** using HTML and CSS inside Python.

📌 **Features:**
- Streamlit layout with fixed footer
- Customizable style and text
- Credits the creator: **Zara Khan**

💻 **Footer Code Snippet:**
```python
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: white;
            background-color: #0e1117;
            padding: 10px;
            font-size: 16px;
            border-top: 1px solid #444;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.3);
        }
    </style>
    <div class="footer">
        Made with ❤️ by <strong>Zara Khan</strong>
    </div>
    """,
    unsafe_allow_html=True
)
🔗 View Code

🚀 Getting Started
Clone the repo:

bash
Copy
Edit
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects
Run any project using:

bash
Copy
Edit
python project_folder/filename.py
For the Streamlit app:

bash
Copy
Edit
streamlit run Streamlit_App/app.py
📚 What I Learned
Basics of Python (variables, loops, conditionals, functions)

String manipulation and pattern printing

Streamlit basics for web UI

Code organization and documentation

📄 License
This repository is licensed under the MIT License.

Created with 💙 by Zara Khan

yaml
Copy
Edit

---

Let me know if you'd like me to auto-generate the folder structure or help organize your repo for GitHub upload!





You said:
projects includes deductive logic game diamond pattern growth mindset library manager unit convertor report card and password generator now modify it and provide me the updated readme file with emojis


ChatGPT said:
Awesome! Here's the updated README.md file with all your projects included:
✅ Deductive Logic Game
✅ Diamond Pattern
✅ Growth Mindset App
✅ Library Manager
✅ Unit Converter
✅ Report Card
✅ Password Generator

With emoji ✨ flair for clarity and personality 👇

📄 README.md — Python Projects by Zara Khan
markdown
Copy
Edit
# 🧠 Python Projects Collection – By Zara Khan

Welcome to my Python Projects Repo! 🚀  
This collection includes beginner-to-intermediate level projects I’ve built during class assignments, all designed to improve logical thinking, problem-solving, and real-world application skills.

---

## 📦 Projects Included

### 1️⃣ 🔐 Password Generator
A secure password generator that creates strong, random passwords using letters, numbers, and special characters.

**🛠 Features:**
- Customizable password length
- Includes upper/lowercase, digits, symbols
- Easy to use and terminal-based

---

### 2️⃣ 📊 Report Card Generator
Generates a student's report card based on entered marks for each subject.

**📌 Features:**
- Accepts multiple subjects
- Calculates total, average, and grade
- Neat and readable output

---

### 3️⃣ 🔁 Unit Converter
Convert units such as:
- Length (meters ↔ kilometers)
- Temperature (Celsius ↔ Fahrenheit)
- Weight (grams ↔ kilograms)

**🔧 Features:**
- Menu-based options
- Simple `if-elif` logic
- Accurate calculations

---

### 4️⃣ 📚 Library Manager
A mini system to manage book borrowing and returns in a library.

**📘 Features:**
- Add/remove books
- Lend books to users
- Keep track of borrowed books
- CLI-based interaction

---

### 5️⃣ 💡 Growth Mindset App
A motivational Streamlit web app to encourage positive thinking.

**🌟 Features:**
- Shows daily affirmations or quotes
- Clean and colorful UI
- Streamlit-based with interactive elements

---

### 6️⃣ 💎 Diamond Pattern Generator
A fun project that prints a centered diamond using `*` characters.

**📐 Output Example (size = 5):**
markdown
Copy
Edit
*
markdown
Copy
Edit
*
yaml
Copy
Edit

---

### 7️⃣ 🧩 Deductive Logic Game
A simple Python guessing game that encourages critical thinking and deduction.

**🎯 Features:**
- Guess the correct number or pattern
- Tracks attempts and gives feedback
- Good for practicing logic and loops

---

## 🛠 How to Run Any Project

1. **Clone the Repository:**
```bash
git clone https://github.com/Zara-Khan-7/Python_Projects.git
cd Python_Projects
Run a Python file:

bash
Copy
Edit
python folder_name/filename.py
For Streamlit Apps (like Growth Mindset):

bash
Copy
Edit
streamlit run folder_name/app.py
🔗 Useful Links
💻 My GitHub Profile: Zara-Khan-7

📚 Python Docs: https://docs.python.org

🧠 Skills Practiced
✅ Loops & Conditionals

✅ Functions & Modular Code

✅ CLI Apps and Streamlit Web Apps

✅ String Manipulation & Input Handling

✅ Creative Problem Solving & Game Logic

📄 License
This repository is licensed under the MIT License.

Made with ❤️ by Zara Khan









