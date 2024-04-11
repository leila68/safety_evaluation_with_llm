from imageai.Detection import VideoObjectDetection
import os
import cv2

def process_video(video_file_path):
    execution_path = os.getcwd()
    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
    detector.loadModel()

    # customize the type of object(s) you want to be detected in the video
    # custom_objects = detector.CustomObjects(person=True, bicycle=True, motorcycle=True)

    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, video_file_path),
                                                 output_file_path=os.path.join(execution_path, "traffic_detected"),
                                                 frames_per_second=20, log_progress=True)
    print(video_path)

    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
    video_detector.loadModel()

    # List to collect object lists per timestamp
    object_list_per_ts = []

    # Function to be called for each second
    def for_seconds(second_number, output_arrays, count_arrays, average_output_count):
        nonlocal object_list_per_ts  # Use nonlocal to modify object_list_per_ts from the outer scope
        object_list_per_ts.append({"average_output_count": average_output_count})

    # Call the function
    video_detector.detectObjectsFromVideo(
        input_file_path=os.path.join(execution_path, video_file_path),
        output_file_path=os.path.join(execution_path, "traffic_detected"),
        frames_per_second=10,
        per_second_function=for_seconds,
        minimum_percentage_probability=30
    )

    # Return the object list per timestamp
    return object_list_per_ts







