"""
Real-time Face Recognition System
Uses webcam to detect and recognize faces from a known faces dataset
"""
import face_recognition
import cv2 
import numpy as np
import os

def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    for file in os.listdir("known_faces"):
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        image_path = os.path.join("known_faces", file)

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print(f"No face found in {file}")   
            continue

        known_face_encodings.append(encodings[0])

        name = os.path.splitext(file)[0]
        known_face_names.append(name)

    return known_face_encodings, known_face_names


FRAME_SCALE = 0.25
TOLERANCE = 0.5

def main():
    # Initialize variables for face detection and recognition
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    # Open webcam (0 = default camera)
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Cannot access webcam")
        return

    known_face_encodings, known_face_names = load_known_faces()
    
    if len(known_face_encodings) == 0:
        print("No known faces found.")
        return

    # Main loop - continuously capture and process video frames
    while True:
        success, frame = video_capture.read()
        if not success:
            print("Failed to read frame.")
            break

        frame = cv2.flip(frame, 1)

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=FRAME_SCALE, fy=FRAME_SCALE)
            small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(small_frame)
            # print(face_locations)

            # If at least one face is detected
            if len(face_locations) > 0:
                # Generate encodings for all detected faces
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)

                face_names = []
                # Loop through each detected face encoding
                for face_encoding in face_encodings:
                    # Compare detected face against all known faces (tolerance 0.5 = sensitivity)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = TOLERANCE)
                    # print(matches)
                    
                    recognized_name = 'Unknown'

                    # Method 1 (commented): Get first matching face index
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     recognized_name = known_face_names[first_match_index]

                    # Method 2 (better): Calculate face distances and find best match
                    # Compute Euclidean distances between detected face and all known faces
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        recognized_name = known_face_names[best_match_index]
                    
                    face_names.append(recognized_name)

                # Draw rectangles and labels on the ORIGINAL frame (not the small one)
                # Scale coordinates back up by 4x because we resized the frame to 1/4
                for (top,right,bottom,left), name in zip(face_locations, face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    # Draw green rectangle around the face
                    frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
                    # Draw filled rectangle behind the name label
                    frame = cv2.rectangle(frame, (left-2, top-35), (right+2, top), (125, 220, 0), cv2.FILLED)

                    cv2.putText(frame, name, (left+5, top-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 20, 255),2)

        # process_this_frame = not process_this_frame

        # Display the resulting video feed
        cv2.imshow('cam', frame)
        # Exit loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()