from gpt4all import GPT4All
def process_prompt(prompt_array):
    semantic_array = []
    for prompt in prompt_array:
        model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")
        output = model.generate(prompt, max_tokens=5)
        semantic_array.append(output)
    return semantic_array





