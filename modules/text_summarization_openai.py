import openai

openai.api_key = "YOUR_API_KEY"

def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "Você é um assistente que resume textos acadêmicos de forma clara e objetiva."},
                {"role": "user", "content": f"Resuma o seguinte texto: {text}"}
            ],
            max_tokens = 300,
            temperature = 0.5
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        print(f"Error generating abstract: {e}")
        return "Abstract unavailable."
