# Gemini Multi-Turn Chat

A Python-based interactive chatbot that uses Google's Gemini AI model to maintain context-aware conversations. This application demonstrates how to implement a multi-turn chat interface with the Gemini API while preserving conversation history.

## Features

- Interactive chat interface with Google's Gemini AI model
- Continuous conversation with no turn limits
- Context preservation across multiple conversation turns
- Configurable model parameters (temperature, top_p, top_k)
- Environment variable-based API key management
- Error handling and graceful exit options

## Prerequisites

- Python 3.7 or higher
- Google Cloud account with Gemini API access
- Gemini API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd gemini-multi-turn-chat
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:
```bash
python app.py
```

2. The chat interface will start, and you can begin conversing with the Gemini model.

3. Type your messages and press Enter to send them.

4. The conversation will continue indefinitely until you type 'quit' to exit.

5. To exit the chat at any time, simply type 'quit' and press Enter.

## Configuration

The script uses the following default configuration:
- Model: gemini-1.5-flash
- Temperature: 1.0
- Top P: 0.9
- Top K: 40

You can modify these parameters in the `app.py` file to suit your needs.

## Dependencies

The project relies on the following Python packages:
- google-generativeai (>=0.3.0)
- python-dotenv (>=1.0.0)

## Error Handling

The script includes comprehensive error handling for:
- Missing API key
- API communication errors
- Invalid user inputs
- Unexpected exceptions
- Keyboard interrupts (Ctrl+C)

## Notes

- The chat maintains context throughout the entire conversation
- Each turn is numbered for reference
- Empty messages are not counted as turns
- The conversation history is preserved until you exit the chat
