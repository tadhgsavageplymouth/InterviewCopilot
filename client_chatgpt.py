#!/usr/bin/env python3
"""
client_chatgpt.py — fetch prompts from OpenAI ChatGPT and forward them to the NAO proxy server
Usage:
    python3 client_chatgpt.py
"""
import socket
import time
import openai

# Configuration
SERVER_IP   = "169.254.242.81"  # NAO proxy server IP
SERVER_PORT = 10000
MODEL       = "gpt-3.5-turbo"    # or whichever ChatGPT model you prefer
PROMPT_ROLE = "assistant"        # role for the conversation messages

# Read OpenAI API key from file
KEY_FILE = r"C:\Users\tsavage2\InterviewCopilot\OpenAIAPIKey.txt"
try:
    with open(KEY_FILE, 'r') as f:
        openai.api_key = f.read().strip()
except Exception as e:
    raise RuntimeError(f"Failed to read API key from {KEY_FILE}: {e}")

# A simple conversation history; you can expand or parameterize this
conversation = [
    {"role": "system", "content": "You are a helpful assistant generating interview questions for a user speaking to a NAO robot."}
]


def fetch_chat_prompt():
    """
    Sends the current conversation context to OpenAI and returns the content of the assistant's reply.
    """
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=conversation,
        temperature=0.7,
    )
    # Extract assistant reply
    message = response.choices[0].message.content.strip()
    # Append to conversation for context
    conversation.append({"role": "assistant", "content": message})
    return message


def main():
    # Create & connect socket to NAO proxy
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print(f"Connecting to {SERVER_IP}:{SERVER_PORT}")
        sock.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected.")

        while True:
            # 1) Fetch next prompt from ChatGPT
            try:
                prompt = fetch_chat_prompt()
            except Exception as e:
                print(f"Error fetching prompt from OpenAI: {e}")
                break

            print(f"Sending to NAO: {prompt}")
            sock.sendall(prompt.encode('utf-8'))

            # 2) Receive acknowledgment
            data = sock.recv(1024)
            if not data:
                print("Server closed connection.")
                break
            print("NAO proxy reply:", data.decode('utf-8'))

            # 3) Optionally pause before next prompt
            time.sleep(2)

if __name__ == "__main__":
    main()
