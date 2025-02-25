from src.dummy import plot_heatmap, plot_loss_curve
from typing import List, Tuple, Union
from src.utils import CSS, JS, GA
from time import time
import gradio as gr
import numpy as np
import os, shutil

start_time = time()


def generate_plots():
    heatmap = plot_heatmap("data/file.txt")
    loss_curve = plot_loss_curve()
    print(num)

    return heatmap, loss_curve


def process_files(file: List[Union[str, bytes]]) -> str:
    if len(file) == 0:
        return "No file uploaded"
    if len(file) > 1:
        return "Upload only one file at a time"

    file = file[0]
    shutil.copyfile(file.name, "./data/file.txt")
    data = open("./data/file.txt", "r").read()
    data = data.strip().split("\n")

    r, c = len(data), len(data[0].split())
    return f"Matrix Dimensions: {r}x{c}"

# Add head=GA("G-ANALYTICS-ID") for google analytics
with gr.Blocks(css=CSS("assets/global.css")) as demo:
    with gr.Row():
        with gr.Column():
            gr.Interface(process_files, inputs="files", outputs="textbox")
            num = gr.Number()

        with gr.Column():
            LC = gr.Plot()
            HM = gr.Plot()

            HM_btn = gr.Button("Generate Heatmap")
            HM_btn.click(generate_plots, inputs=[], outputs=[HM, LC])

os.makedirs("data", exist_ok=True)
demo.launch()
