
# export OPENAI_API_KEY="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"
from langchain_openai import OpenAI


llm = OpenAI(openai_api_key="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")

llm.invoke(
    "What are some theories about the relationship between unemployment and inflation?"
)

for chunk in llm.stream(
    "What are some theories about the relationship between unemployment and inflation?"
):
    print(chunk, end="", flush=True)