def load_conversations(file_path):
    import json
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_conversations(file_path, conversations):
    import json
    with open(file_path, 'w') as file:
        json.dump(conversations, file, indent=4)

def add_conversation(conversations, user_input, llm_response):
    conversations.append({
        "user_input": user_input,
        "llm_response": llm_response
    })