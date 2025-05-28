import google.generativeai as genai
from dotenv import load_dotenv, get_key

def chat_with_gemini():
    """
    Creates a simple interactive chatbot using the Google Gemini API,
    preserving context across turns and demonstrating model parameter usage.
    """
    try:
        # Load environment variables from .env file
        load_dotenv()
        api_key = get_key('.env', 'GEMINI_API_KEY')
        if not api_key:
            print("Error: GEMINI_API_KEY not found in .env file.")
            return
        genai.configure(api_key=api_key)

        # --- Model Configuration ---
        model_name = "gemini-1.5-flash"

        temperature = 1.0
        generation_config = genai.types.GenerationConfig(
            temperature=temperature,
            top_p=0.9,
            top_k=40
        )

        # Initialize the generative model
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config
        )

        # Start a chat session (this preserves history)
        chat = model.start_chat(history=[]) # Start with an empty history

        print(f"\nChatting with {model_name} (Temperature: {temperature}). Type 'quit' to end.")
        print("-" * 30)

        # --- Conversation Loop ---
        turn_count = 0

        while True:
            turn_count += 1
            print(f"\n--- Turn {turn_count} ---")

            user_input = input("You: ")
            if user_input.lower() == 'quit':
                print("Exiting chat.")
                break

            if not user_input.strip():
                print("Please enter a message.")
                turn_count -= 1 # Don't count empty inputs as a turn
                continue

            try:
                # Send message to Gemini, history is automatically managed by chat object
                response = chat.send_message(user_input)
                model_response_text = response.text
                print(f"Gemini: {model_response_text}")

            except Exception as e:
                print(f"Error sending message or receiving response: {e}")
                # If an API error occurs, you might want to break or allow retry
                break

        if turn_count == 0:
            print("No conversation occurred.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Initializing Context-Aware Gemini Chat...")
    chat_with_gemini()