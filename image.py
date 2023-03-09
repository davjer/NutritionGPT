import os

import openai

PROMPT = "IA artificial futuristic creature in the style of realistic"


openai.api_key = "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"


response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])