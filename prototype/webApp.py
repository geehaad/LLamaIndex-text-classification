import sys
sys.path.insert(0, 'D:\Arabot\LLama') # add your path here
import pandas as pd
import gradio as gr
from src.components.helper import analyze_text, analyze_file



# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("Text Classification")

    # Tab for answer_questions func 
    with gr.Tab("Text"):
        txt_input = gr.Textbox(label="context", type="text", placeholder="Enter context here...", lines=5)
        labelT_input = gr.Textbox(label="Labels", type="text",placeholder="Enter how you want to classify the text here...")
        txt_button = gr.Button("Get Classification")
        txt_output = gr.Textbox(label="Answer", type="text", placeholder="Answer will be displayed here...")

    txt_button.click(analyze_text, inputs=[txt_input, labelT_input], outputs=txt_output)

    # Tab for answer_questions func 
    with gr.Tab("Files"):
        file_input = gr.File(label="context")
        labelF_input = gr.Textbox(label="Labels", type="text",placeholder="Enter how you want to classify the text here...")
        file_button = gr.Button("Get Classification")
        file_output = gr.Textbox(label="Answer", type="text", placeholder="Answer will be displayed here...")

    # Function to handle file input and call analyze_file
    def file_handler(file, labels):
        # Get the file path from the temporary file object
        file_path = file.name
        return analyze_file(file_path, labels)
    
    file_button.click(file_handler, inputs=[file_input, labelF_input], outputs=file_output)

# Launch the Gradio interface
demo.launch()