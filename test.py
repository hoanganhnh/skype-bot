import openai

openai.api_key = "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"

def render_text(prompt):
    model = "text-davinci-003"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

    generated_text = response.choices[0].text
    return generated_text
 
 
print(render_text('What is BS Commerce company ?'))