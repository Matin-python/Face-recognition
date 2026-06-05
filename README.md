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
cd face-recognition
```

### 2. Create a virtual environment (optional)

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

## Usage

### Add Known Faces

Place images of people you want the system to recognize inside the `known_faces` folder.

Example:

```text
known_faces/
├── Matin.jpg
├── Mahdi.jpg
├── Sara.jpg
```

The filename (without extension) will be used as the person's name.

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
6. Finds the closest match using face distance.
7. Draws a bounding box and displays the person's name.

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

Mohammad Reza Bakhshandeh

Bachelor's Degree in Electrical Engineering (Electronics)

Learning Python, Computer Vision, and Artificial Intelligence.
