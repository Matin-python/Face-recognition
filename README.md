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
├── face recognize.py
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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


## Troubleshooting Installation

The `face_recognition` library depends on `dlib`.

First, try installing `dlib` using:

```bash
pip install dlib
```

If you encounter installation errors while building `dlib`, install **CMake** first and then try again:

```bash
pip install cmake
pip install dlib
```

> **Note:** Installing `CMake` may not be necessary on all systems because precompiled `dlib` packages are available for many Python versions.

### Installing `dlib` Manually (Windows)

If you are using **Windows** and still cannot install `dlib`, you can download a precompiled wheel from the following **community-maintained** repository:

https://github.com/Murtaza-Saeed/Dlib-Precompiled-Wheels-for-Python-on-Windows-x64-Easy-Installation

Download the wheel file that matches your Python version.

For example, if you are using **Python 3.12.x**, download:

```text
dlib-19.24.99-cp312-cp312-win_amd64.whl
```

After downloading the file:

1. Move the `.whl` file to a folder of your choice.
2. Open **Command Prompt** in that folder.
3. Run the following command:

```bash
pip install dlib-19.24.99-cp312-cp312-win_amd64.whl
```

> **Tip:** In Windows, you can quickly open Command Prompt in a folder by typing **`cmd`** in the File Explorer address bar and pressing **Enter**.

> **Note:** This repository is maintained by the community and is not an official `dlib` release. If it becomes unavailable or does not contain a wheel for your Python version, you may need to build `dlib` from source or look for another compatible precompiled wheel.


## NumPy Compatibility

If you encounter the following error:

```text
RuntimeError: Unsupported image type, must be 8bit gray or RGB image.
```

your installed version of **NumPy** is likely too new.

Some versions of `dlib` are not compatible with **NumPy 2.x**. In that case, install a version of NumPy **below 2.0** (see `requirements.txt`).

> **Note:** Your installed version of **OpenCV (`cv2`)** must also be compatible with your NumPy version. Otherwise, the project may fail to run due to dependency conflicts.


## Installing `face_recognition_models`

If you encounter the following message when running the project:

```text
Please install `face_recognition_models` with this command before using `face_recognition`:
```

install the required models by running:

```bash id="abmu67"
pip install git+https://github.com/ageitgey/face_recognition_models
```

Then run the application again.

If the same message still appears after installing `face_recognition_models`, the issue may be caused by an incompatible version of `setuptools`.

Try installing an older version of `setuptools`:

```bash id="6fjlwm"
pip install setuptools==80.10.2
```

After downgrading `setuptools`, install `face_recognition_models` again:

```bash id="2vdyqr"
pip install git+https://github.com/ageitgey/face_recognition_models
```

Then run the application again.


## Tested Environment

This project has been tested on:

* Windows 11
* Python 3.12
* `face_recognition = 1.2.3`
* `dlib = dlib-19.24.99-cp312-cp312-win_amd64.whl`
* `opencv-python = 4.10.0.84`
* `NumPy = 1.26.4`


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
python face recognize.py
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
