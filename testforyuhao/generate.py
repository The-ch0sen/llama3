import ollama

question_1 = "What is 2+2?"

ans_1 = "2 + 2 equals 4. This is a basic arithmetic operation where you are " \
        "adding the number 2 to another number 2, resulting in 4."

question_2 = "Add 3 onto the last answer. What is it now?"

prompt = f"""<|user|>
{question_1}<|end|>
<|assistant|>
{ans_1}<|end|>
<|user|>
{question_2}<|end|>
<|assistant|>
"""

response = ollama.generate(
    model="phi3",
    prompt=prompt
)

print(response["response"])