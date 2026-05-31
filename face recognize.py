import face_recognition
import cv2 
import numpy as np

matin_face = face_recognition.load_image_file('Matin.jpg')
matin_face_location = face_recognition.face_locations(matin_face)
print(matin_face_location)

face_landmarks_list = face_recognition.face_landmarks(matin_face)
# print(face_landmarks_list)

# matin_face2 = cv2.cvtColor(matin_face, cv2.COLOR_RGB2BGR)
# matin_face2 = cv2.rectangle(matin_face2, (matin_face_location[0][3], matin_face_location[0][0]), (matin_face_location[0][1], matin_face_location[0][2]), (0, 255, 0), 3)
# matin_face2 = cv2.resize(matin_face2, (300, 400))
# cv2.imshow('image', matin_face2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

mahdi_face = face_recognition.load_image_file('Mahdi.jpg')
mahdi_face_location = face_recognition.face_locations(mahdi_face)

matin_face_encoding = face_recognition.face_encodings(matin_face)[0]
mahdi_face_encoding = face_recognition.face_encodings(mahdi_face)[0]

known_face_encodings = [
    matin_face_encoding,
    mahdi_face_encoding
]

known_face_names = [
    'Matin',
    'Mahdi'
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 1)

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(small_frame)
        # print(face_locations)

        if len(face_locations) > 0:
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.5)
                print(matches)
                
                name_temp = 'Unknown'

                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name_temp = known_face_names[first_match_index]

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name_temp = known_face_names[best_match_index]
                
                face_names.append(name_temp)

            for (top,right,bottom,left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
                frame = cv2.rectangle(frame, (left-2, top-35), (right+2, top), (125, 220, 0), cv2.FILLED)

                cv2.putText(frame, name, (left+5, top-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (20, 20, 255),2)

    # process_this_frame = not process_this_frame

    cv2.imshow('cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()