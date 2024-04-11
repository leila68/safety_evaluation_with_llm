from gpt4all import GPT4All

def generate_warning_message(prompt_message):
    # Initialize the GPT-4 model
    model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")

    # Generate text based on the content of the text file as prompt
    message = model.generate(prompt_message, max_tokens=150)

    # Print the generated text
    print(message)
    return message

