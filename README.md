# English Practice CLI

This project is a command-line interface (CLI) application designed to help users practice their written English using a large language model (LLM) like ChatGPT. The application allows users to engage in conversations, receive feedback, and track their progress over time.

## Project Structure

```
english-practice-cli
├── main.py                # Entry point of the application
├── cli                    # Contains command definitions for the CLI
│   └── commands.py
├── llm                    # Handles connection to the OpenAI API
│   └── openai_api.py
├── storage                # Manages loading and saving of conversation data
│   └── json_storage.py
├── data                   # Contains conversation data in JSON format
│   └── conversations.json
├── requirements.txt       # Lists project dependencies
└── README.md              # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd english-practice-cli
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the application, run the following command in your terminal:
```
python main.py
```

### Commands

- `practice`: Engage in a conversation with the LLM to practice English writing.
- `history`: View your previous conversations and responses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.