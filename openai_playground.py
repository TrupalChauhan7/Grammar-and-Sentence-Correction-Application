import openai

GPT3_MODELS = {
    'davinci': 'gpt-3.5-turbo-16k',  # Use gpt-4 as the default model
}


class OpenAIPlayground:
    def __init__(self, api_key):
        self.openai = openai
        self.openai.api_key = api_key

    def grammar_checker(self, prompt, model=GPT3_MODELS['davinci'], temperature=0.0, max_tokens=1000, top_p=1.0,
                        frequency_penalty=0.0, presence_penalty=0.0):
        # Use ChatCompletion API
        response = self.openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that corrects grammar."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        # Extract and return the result
        result = {
            'id': response['id'],
            'created': response['created'],
            'model': response['model'],
            'completion_tokens': response['usage']['completion_tokens'],
            'prompt_tokens': response['usage']['prompt_tokens'],
            'total_tokens': response['usage']['total_tokens'],
            'outputs': response['choices'][0]['message']['content'],
            'status': response['choices'][0]['finish_reason']
        }
        return result


# Example usage
if __name__ == "__main__":
    api_key = "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"  # Replace with your OpenAI API key
    playground = OpenAIPlayground(api_key)

