import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    # Open the default camera
    cap = cv2.VideoCapture(0)  # Use index 0 for the internal camera

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    print("Scanning QR code. Press 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Decode the QR codes in the frame
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Draw a rectangle around the QR code
            points = obj.polygon
            if len(points) == 4:
                pts = [point for point in points]
                pts = pts + [pts[0]]  # Complete the polygon
                for i in range(len(pts) - 1):
                    cv2.line(frame, pts[i], pts[i + 1], (0, 255, 0), 3)

            # Extract the decoded text
            qr_text = obj.data.decode('utf-8')
            print("Detected QR code:", qr_text)

            # Draw the text near the QR code
            cv2.putText(frame, qr_text, (points[0].x, points[0].y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
