import ollama

question_1 = "What is 2+2?"

ans_1 = "2 + 2 equals 4. This is a basic arithmetic operation where you are " \
        "adding the number 2 to another number 2, resulting in 4."

question_2 = "Add 3 onto the last answer. What is it now?"

response = ollama.chat(
    model="phi3",
    messages=[
        {"role": "user", "content": question_1},
        {"role": "assistant", "content": ans_1},
        {"role": "user", "content": question_2}
    ]
)

print(response["message"]["role"])
print(response["message"]["content"])