import cv2
from pyzbar import pyzbar

def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print("Detected barcode:", obj)
        image = draw_barcode(obj, image)
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

        # Save the barcode data to a text file
        with open("barcode_data.txt", "a") as file:
            file.write(f"Type: {obj.type}, Data: {obj.data}\n")

    return image

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0), thickness=5)
    return image

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = decode(frame)

    cv2.imshow("Barcode Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
