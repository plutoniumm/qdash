from src.dummy import plot_heatmap, plot_loss_curve
from src.utils import CSS, JS, GA, Event
from logging import basicConfig, INFO
from typing import List, Union
from shutil import copyfile
from time import time
import gradio as gr
import os

start_time = time()
basicConfig(
    level=INFO,
    filemode="a",
    filename="data/main.log",
    format="%(asctime)s - %(message)s",
)


def generate_plots():
    Event("Generating Plots", "INFO", "generate_plots")
    heatmap = plot_heatmap("data/file.txt")
    loss_curve = plot_loss_curve()

    return heatmap, loss_curve


def process_files(file: List[Union[str, bytes]], epochs, iterations, tol) -> str:
    if len(file) == 0:
        Event("0 Files sent", "WARN", "process_files")
        return "No file uploaded"
    if len(file) > 1:
        Event(f"{len(file)} Files sent", "WARN", "process_files")
        return "Upload only one file at a time"

    file = file[0]
    copyfile(file.name, "./data/file.txt")
    data = open("./data/file.txt", "r").read()
    data = data.strip().split("\n")

    r, c = len(data), len(data[0].split())
    Event(f"Matrix Dim: {r}x{c}", "INFO", "process_files")
    return f"Mat Dim: {r}x{c} @ {epochs} epochs, {iterations} its <tol={tol}"


gr.set_static_paths(paths=["data/"])
with gr.Blocks(css=CSS("global.css")) as demo:
    with gr.Row():
        with gr.Column():
            gr.Interface(
                process_files,
                [
                    "files",
                    gr.Number(value=100),
                    gr.Number(value=100),
                    gr.Number(value=1e-3),
                ],
                outputs="textbox",
                flagging_mode="never",
            )

        with gr.Column():
            LC = gr.Plot()
            HM = gr.Plot()

            HM_btn = gr.Button("Generate Heatmap")
            HM_btn.click(generate_plots, inputs=[], outputs=[HM, LC])

os.makedirs("data", exist_ok=True)
demo.launch()
# demo.launch(share=True)
