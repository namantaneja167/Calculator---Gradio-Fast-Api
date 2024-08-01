import gradio as gr
import requests

# A list to store the last 5 operations
operation_history = []
BASE_API = 'http://127.0.0.1:8000'

# Function to perform the calculation and handle errors
def general_api(a,b,operation):
            r = requests.get(BASE_API + f'/{operation}/{a}/{b}')
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()[0]
                if operation == 'addition':
                    operation_history.append(f"Addition of {a} + {b} = {data}")
                elif operation == 'subtraction':
                    operation_history.append(f"Subtraction of {a} - {b} = {data}")
                elif operation == 'multiplication':
                    operation_history.append(f"Multiplication of {a} * {b} = {data}")
                elif operation == 'division':
                    operation_history.append(f"Division of {a}/{b} = {data}")
                # Keep only the last 5 operations
                if len(operation_history) > 5:
                    operation_history.pop(0)
                return data, "\n".join(operation_history)
            elif r.status_code == 404:
                message = f"Error: Invalid API Endpoint. Status code: {r.status_code}"
                return message,message
            else:
                message = f"Error: Unable to fetch data. Status code: {r.status_code}"
                operation_history.append(f"Error Occured : Status code {r.status_code}")
                if len(operation_history) > 5:
                    operation_history.pop(0)
                return message, "\n".join(operation_history)

# Gradio UI components
with gr.Blocks(theme="dark") as calculator:
    gr.Markdown("# Advanced Calculator", elem_id="header")
    gr.Markdown("### Enter your numbers and select an operation:", elem_id="header")

    with gr.Row():
        num1_input = gr.Number(label="Number 1")
        num2_input = gr.Number(label="Number 2")

    with gr.Row():
        add_button = gr.Button("Add")
        sub_button = gr.Button("Subtract")
        mul_button = gr.Button("Multiply")
        div_button = gr.Button("Divide")

    result_output = gr.Textbox(lines=1, label="Result")
    history_output = gr.Textbox(lines=5, label="Last 5 Operations", interactive=False)

    
    # Define the operations
    def add(a, b):
        return general_api(a,b,"addition")
    
    def subtract(a, b):
        return general_api(a,b,"subtraction")

    def multiply(a, b):
        return general_api(a,b,"multipdlication")

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero", "\n".join(operation_history)
        return general_api(a,b,"division")

    # Set up button clicks
    add_button.click(add, inputs=[num1_input, num2_input], outputs=[result_output, history_output])
    sub_button.click(subtract, inputs=[num1_input, num2_input], outputs=[result_output, history_output])
    mul_button.click(multiply, inputs=[num1_input, num2_input], outputs=[result_output, history_output])
    div_button.click(divide, inputs=[num1_input, num2_input], outputs=[result_output, history_output])

# Launch the Gradio app
calculator.launch()