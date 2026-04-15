import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


print("------------------Starting Virtual Assistant------------------")
while True:
    user_input = input("User---> ").strip()  

    if user_input.lower() == "end": 
        print("------------------Thanks for using------------------")
        break
    else:
        system_prompt = """ 
        Suppose you are Gafadigpt
        You are a friendly virtual assistant.
        Respond to user input in a clear, short, and easy-to-read way.
        Keep answers polite, helpful, and concise.
        And my name is Prasil so always greet me back in starting if i say if i greet you
        """

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.4,
            max_completion_tokens=1024,
        )

        print("\nAssistant--->", completion.choices[0].message.content, "\n")
