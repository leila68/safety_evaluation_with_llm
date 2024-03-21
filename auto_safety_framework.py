from video_object_detection import process_video
from generate_prompt import generate_prompt
from gpt4all_model import generate_warning_message
from llm_module import *



import sys

video_file_path = sys.argv[1]
object_list = process_video(video_file_path)
print("main:", object_list)
prompt_array = generate_prompt(object_list)
print("main:", prompt_array)
# warning_message = generate_warning_message(prompt_array)
