import face_recognition
import cv2

# Load known image and encode it
known_image = face_recognition.load_image_file("my_image.jpg")  # Replace with your known face image
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load the image to recognize
image_path = "test_image3.jpg"  # Replace with the image you want to test
image = face_recognition.load_image_file(image_path)

# Find all faces and encodings in the image
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

# Load the image in OpenCV format to draw results
image_cv2 = cv2.imread(image_path)

# Compare faces
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([known_encoding], face_encoding)

    if True in matches:
        label = "Match Found"
        color = (0, 255, 0)  # Green for match
    else:
        label = "No Match"
        color = (0, 0, 255)  # Red for no match

    # Draw rectangle around face
    cv2.rectangle(image_cv2, (left, top), (right, bottom), color, 2)
    cv2.putText(image_cv2, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Show the result
cv2.imshow("Face Recognition", image_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
