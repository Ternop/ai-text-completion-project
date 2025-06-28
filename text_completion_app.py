# text_completion_app.py
# Andrew Ternopolsky
import openai  # Import the OpenAI library to interact with the API
import os      # Import os to access environment variables

# Get the API key from an environment variable (for security)
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    print("=== AI Text Completion App ===\n")

    # Loop to allow multiple prompts until the user types 'exit'
    while True:
        user_prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if user_prompt.strip().lower() == "exit":
            break

        # Ask for temperature and max tokens, with default values if input is empty or invalid
        try:
            temperature = float(
                input("Temperature (0.0–1.0, default 0.7): ") or 0.7)
            max_tokens = int(input("Max tokens (default 150): ") or 150)
        except ValueError:
            print("Invalid input. Using default parameters.")
            temperature = 0.7
            max_tokens = 150

        # Try to send the prompt to the OpenAI API and get a response
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            # Print the AI's response to the terminal
            print("\nAI Response:\n",
                  response.choices[0].message.content, "\n")

        # If anything goes wrong (like no quota), print the error
        except Exception as e:
            print("Error:\n", e)


# Entry point: run the app if this script is being executed directly
if __name__ == "__main__":
    main()
