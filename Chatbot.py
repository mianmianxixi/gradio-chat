import openai
import gradio as gr

openai.api_key = ""  # Replace with your key

def update_txt(txt):
    openai.api_key = txt

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,
        temperature=1.0,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message


with gr.Blocks() as demo:
    gr.Markdown('# Q&A Bot with OpenAI Models')
    with gr.Tab("Input Text Document"):
        txt_box = gr.Textbox(label="API Key", type='password')
        txt_box.blur(fn=update_txt,inputs=[txt_box])
        gr.ChatInterface(predict)


demo.queue().launch(server_name="0.0.0.0")
