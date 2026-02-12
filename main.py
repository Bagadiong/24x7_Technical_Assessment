from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from 24x7-technical-assessment!")
    llm = ChatBedrockConverse(
        model_id="openai.gpt-oss-120b-1:0",
        region_name="ap-northeast-1",
        aws_access_key_id= os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        temperature=0
    )
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg)
    print(ai_msg.content)

if __name__ == "__main__":
    main()
