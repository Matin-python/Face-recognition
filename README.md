# Real-Time Face Recognition System

A Python-based real-time face recognition application that uses a webcam to detect and identify known individuals using the `face_recognition` library and OpenCV.

## Features

* Real-time face detection from webcam feed
* Face recognition using facial encodings
* Displays detected person's name above their face
* Supports multiple known faces
* Labels unknown faces as **Unknown**
* Uses efficient face distance comparison for better accuracy

## Technologies Used

* Python 3
* OpenCV (`cv2`)
* NumPy
* face_recognition

## How It Works

1. Load images of known individuals.
2. Generate 128-dimensional facial encodings.
3. Open the webcam and capture video frames.
4. Detect faces in each frame.
5. Compare detected faces against known encodings.
6. Display the recognized person's name on the screen.

## Project Structure

```text
project/
│
├── main.py
├── Matin.jpg
├── Mahdi.jpg
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/face-recognition-system.git
cd face-recognition-system
```

### 2. Install dependencies

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
```

Or:

```bash
pip install -r requirements.txt
```

## Usage

1. Add images of known people to the project directory.
2. Update the image filenames and names in the code.
3. Run the application:

```bash
python main.py
```

4. A webcam window will open.
5. Press **Q** to quit.

## Example

When a known face appears in front of the camera:

```text
Matin
```

When an unknown face appears:

```text
Unknown
```

## Recognition Process

The application:

* Detects faces in each frame
* Generates facial encodings
* Compares encodings with known faces
* Calculates face distances
* Selects the closest valid match
* Draws a bounding box and name label

## Future Improvements

* Load known faces automatically from a folder
* Store face data in a database
* Add face registration functionality
* Improve performance with frame skipping
* Add confidence score display
* Support multiple cameras
* Create a graphical user interface (GUI)

## Notes

* Good lighting improves recognition accuracy.
* High-resolution images produce better facial encodings.
* Recognition accuracy depends on image quality and face visibility.

## License

This project is open-source and available under the MIT License.

## Author

Mohammad Reza Bakhshandeh
