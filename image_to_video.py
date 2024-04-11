import os
import cv2


def images_to_video(input_dir, output_file, fps=30):
    # Get all image files from the input directory
    image_files = sorted(
        [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(('.png', '.jpg', '.jpeg'))])

    if not image_files:
        print("No image files found in the input directory.")
        return

    # Get the dimensions of the first image
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Write each image to the video
    for image_file in image_files:
        image = cv2.imread(image_file)
        out.write(image)

    # Release the VideoWriter object
    out.release()
    print("Video created successfully.")


# Example usage
input_directory = "C:/Users/Leila/safety_evaluation_with_llm/kittimots/video3"
output_video = "output_video3.mp4"
images_to_video(input_directory, output_video)
