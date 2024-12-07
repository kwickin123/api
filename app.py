import openai


API_KEY = input("Enter your api Key:)

openai.api_key = API_KEY


chat_log = []

while True:
    user_message = input("User:")
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role" : "user", "content": user_message })
        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [{"role": "user", "content": user_message}]
            )
        output_msg = response["choices"][0]["message"]["content"]
        print("CHATGPT:", output_msg)


