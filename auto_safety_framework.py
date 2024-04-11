from video_object_detection import process_video
from generate_prompt import generate_prompt

import sys
import os

video_file_path = sys.argv[1]
object_list = process_video(video_file_path)
# object_list = process_image(video_file_path)
# print("main:", object_list)
prompt_array = generate_prompt(object_list)
print("main:", prompt_array)
# if GPT license is provided, set below to True
GPT_LIC = False
if GPT_LIC:
    # call gpt
    llm_out = ""
else:
    # extract file name to print
    file_name = os.path.basename(video_file_path)
    # load from gpt message_warning.txt
    # Check if the file name contains "output_video1"
    if "output_video1" in file_name:
        # If yes, read and print the content of output_message_video1 file
        with open('output_message_video1.txt', 'r') as file:
            print("Message for ", file_name, ": ", file.read())
    # Check if the file name contains "output_video2"
    elif "output_video2" in file_name:
        # If yes, read and print the content of output_message_video2 file
        with open('output_message_video2.txt', 'r') as file:
            print("Message for ", file_name, ": ", file.read())
    elif "output_video3" in file_name:
        # If yes, read and print the content of output_message_video2 file
        with open('output_message_video3.txt', 'r') as file:
            print("Message for ", file_name, ": ", file.read())
    else:
        print("Invalid file name.")
