# import cv2
# from ultralytics import YOLO

# 1. Load a pre-trained model (Nano version is fastest for real-time)
# model = YOLO("yolov8n.pt") 

# 2. Open the webcam (0 is usually the default camera)
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, frame = cap.read()
    # if not success:
    #     break

    # 3. Run YOLO detection on the frame
    # 'stream=True' is more memory-efficient for video
    # results = model(frame, stream=True)

    # 4. Visualize the results on the frame
    # for r in results:
    #     annotated_frame = r.plot()

    # 5. Display the output
    # cv2.imshow("Real-time Detection", annotated_frame)

    # Break loop on 'q' key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()