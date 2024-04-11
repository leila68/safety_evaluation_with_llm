def generate_prompt(object_list):
    file_path = "prompt_strings.txt"
    with open(file_path, 'w') as file:
        all_prompt_strings = []
        for data in object_list:
            average_output_count = data['average_output_count']

            # Extract counts for each object type
            person = average_output_count.get('person', 0)
            car = average_output_count.get('car', 0)
            motorbike = average_output_count.get('motorbike', 0)
            bus = average_output_count.get('bus', 0)
            bicycle = average_output_count.get('bicycle', 0)

            # Construct the desired strings
            prompt_string1 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Give a warning message according to the objects"
                              f" that are detected in the environment")

            prompt_string2 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Is this environment safe for driving?")

            prompt_string3 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Should the driver be more careful during driving?")

            prompt_string4 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Is it necessary to give the driver warning during"
                              f" driving in this environment?")

            prompt_string5 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Is this place crowded or not? ")

            prompt_string6 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Is there any danger alarm in this environment for"
                              f" driver?")

            prompt_string7 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. should the driver be more caution"
                              f" during driving in this environment?")

            prompt_string8 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. what is dangerous during driving in the environment?")

            prompt_string9 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                              f" and {bus} bus in the environment. Is there many cars in the environment?")

            prompt_string10 = (f"There are {person} person, {bicycle} bicycle, {car} car, {motorbike} motorbike,"
                               f" and {bus} bus in the environment. Is there many pedestrian in the environment? ")

            prompt_string11 = ("According to the scene perception give a message to the driver.")
            # Append all prompt strings
            all_prompt_strings.extend([prompt_string1, prompt_string2, prompt_string3, prompt_string4, prompt_string5,
                                       prompt_string6, prompt_string7, prompt_string8, prompt_string9, prompt_string10,
                                       prompt_string11])

        # Write all prompt strings to the file
        file.write('\n'.join(all_prompt_strings))

    return all_prompt_strings



