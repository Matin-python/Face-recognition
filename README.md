# Real-Time Face Recognition System

A Python application that performs real-time face detection and recognition using a webcam. The system automatically loads known faces from a folder, generates facial encodings, and identifies people in live video streams.

## Features

* Real-time face detection and recognition
* Automatic loading of known faces from a directory
* Supports multiple known individuals
* Labels unknown faces as "Unknown"
* Webcam validation and error handling
* Face encoding validation for uploaded images
* Easy to extend by adding new images to the dataset

## Technologies Used

* Python 3
* OpenCV
* face_recognition
* NumPy

## Project Structure

```text
face-recognition-system/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── known_faces/
    ├── Person1.jpg
    ├── Person2.jpg
    └── Person3.jpg
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Matin-python/Face-recognition.git
cd Face-recognition
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## First-Time Setup for face_recognition

The `face_recognition` library depends on `dlib`.

Install dlib using:

```bash
pip install dlib
```

If you encounter installation errors related to building dlib, install CMake and try again:

```bash
pip install cmake
pip install dlib
```

This step may not be necessary on all systems because precompiled dlib packages are available for many Python versions.

## Usage

### Add Known Faces

Before running the application, you must add at least one image to the `known_faces` directory.

Example:

```text
known_faces/
├── Matin.jpg
├── Mahdi.jpg
├── Sara.jpg
```

The filename (without the extension) will be used as the person's name during recognition.

**Important:** If the `known_faces` folder is empty, the system will not be able to recognize anyone.

### Run the Application

```bash
python main.py
```

### Controls

* Press **Q** to quit the application.

## How It Works

1. Loads all images from the `known_faces` folder.
2. Generates face encodings for each valid image.
3. Opens the webcam feed.
4. Detects faces in each frame.
5. Compares detected faces against known encodings.
6. Calculates face distances and finds the closest match.
7. Draws a bounding box and displays the detected person's name.

## Example Output

### Known Face

```text
Matin
```

### Unknown Face

```text
Unknown
```

## Error Handling

The application checks for:

* Missing webcam access
* Invalid image files
* Images without detectable faces
* Empty face database

Example messages:

```text
Cannot access webcam
```

```text
No face found in Sara.jpg
```

```text
No known faces found.
```

## Future Improvements

* Face registration through the webcam
* Graphical User Interface (GUI)
* Face recognition confidence scores
* Attendance logging system
* Database integration
* Performance optimization with frame skipping
* Multi-camera support

## License

This project is licensed under the MIT License.

## Author

**Mohammad Reza Bakhshandeh**

Electrical Engineering (Electronics) Graduate

Interested in Python Development, Computer Vision, Machine Learning, and Artificial Intelligence.
