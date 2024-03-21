

def generate_prompt(object_list):
    prompt_string = ""
    for data in object_list:
        average_output_count = data['average_output_count']

        # Extract counts for each object type
        person = average_output_count.get('person', 0)
        car = average_output_count.get('car', 0)
        motorbike = average_output_count.get('motorbike', 0)
        bus = average_output_count.get('bus', 0)
        bicycle = average_output_count.get('bicycle', 0)

        # Construct the desired string
        prompt_string = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                         f" and {bus} bus in the environment. give a warning message according to the objects "
                         f"that are detected in the environment")
        print(prompt_string)

    return prompt_string
