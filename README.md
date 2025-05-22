# Convert Color Image to Sketch

Transform your color photos into pencil sketches with this simple, interactive web app.

[Live Demo](https://convert-color-image-to-sketch-2025.streamlit.app/)

---

## 📖 Project Information

**Convert Color Image to Sketch** is a web application that enables users to upload any color image and instantly convert it into a pencil sketch. The project aims to make artistic photo transformation accessible to everyone, using efficient image processing techniques. The app is ideal for creative users, educators, and anyone interested in digital art or computer vision.

**Key Features:**
- Upload color images (JPG, PNG)
- Instant pencil sketch conversion
- Download the sketch output
- Clean, user-friendly web interface

---

## 🛠️ Technology Overview

| Technology   | Purpose                                                      |
|--------------|--------------------------------------------------------------|
| Python       | Core programming language                                    |
| Streamlit    | Rapid web app development and deployment                     |
| OpenCV       | Image processing and sketch effect transformation            |
| NumPy        | Efficient numerical operations and image array manipulation  |

**How It Works:**
1. **Image Upload:** Users upload a color image via the web interface.
2. **Processing Pipeline:**
   - The image is converted to grayscale.
   - The grayscale image is inverted.
   - A Gaussian blur is applied to the inverted image.
   - The blurred, inverted image is blended with the grayscale image using a dodge technique, creating a pencil sketch effect.
3. **Result:** The sketch is displayed and can be downloaded by the user.

---

## 🚀 Getting Started

1. **Clone the repository:**
    ```
    git clone https://github.com/BrijeshRakhasiya/Convert-Color-Image-to-Sketch.git
    cd convert-color-image-to-sketch
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```
    streamlit run app.py
    ```

---

## 📄 Requirements

- Python 3.9–3.13
- Streamlit
- OpenCV (`opencv-python`)
- NumPy

---

## 📷 Example

| Original Image | Sketch Output |
|:--------------:|:------------:|
| ![original](/smile_img.jpg) | ![sketch](/sketch_img.png) |

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue to discuss what you would like to change.

---

## 📫 Contact

For questions, open an issue or contact [brijeshrakhasiya.aiml@gmail.com](mailto:brijeshrakhasiya.aiml@gmail.com).
