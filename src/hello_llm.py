import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def ask(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are concise."},
          {"role": "user", "content": question}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
  q = " ".join(sys.argv[1:]) or "Say hello in one sentence."
  print(ask(q))