from click import command, option, echo
import json
from storage.json_storage import load_conversations, save_conversations
from llm.openai_api import send_message_to_llm

@command()
@option('--text', prompt='Enter your text', help='The text you want to practice with.')
def practice(text):
    """Practice English by sending text to the LLM and receiving a response."""
    response = send_message_to_llm(text)
    echo(f"LLM Response: {response}")
    conversation = {'user_input': text, 'llm_response': response}
    # Load existing conversations first, then add new one and save
    conversations = load_conversations('./conversations.json')
    conversations.append(conversation)
    save_conversations('./conversations.json', conversations)
    echo("Conversation saved.")

@command()
def history():
    """Display the history of conversations."""
    conversations = load_conversations('./conversations.json')
    if not conversations:
        echo("No conversation history found.")
    else:
        for index, conversation in enumerate(conversations):
            echo(f"{index + 1}. User: {conversation['user_input']}")
            echo(f"   LLM: {conversation['llm_response']}")