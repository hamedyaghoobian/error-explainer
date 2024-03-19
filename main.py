import time
import threading
from tkinter import Tk, messagebox
import httpx
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip

# Controller for simulating keyboard inputs
controller = Controller()

# OLLAMA endpoint and configuration for explaining coding errors
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "codellama",  #  A large language model that can use text prompts to generate and discuss code. 
    "keep_alive": "5m",
    "stream": False,
}

# Template for the OLLAMA prompt to explain coding errors
PROMPT_TEMPLATE = """Explain the following coding error in detail:
$error
"""

# Initialize tkinter in a thread-safe way
root = Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

def explain_error(error):
    prompt = PROMPT_TEMPLATE.replace("$error", error)
    try:
        response = httpx.post(
            OLLAMA_ENDPOINT,
            json={"prompt": prompt, **OLLAMA_CONFIG},
            headers={"Content-Type": "application/json"},
            timeout=20,  # Increased timeout
        )
        response.raise_for_status()  # Raise an exception for HTTP error responses
        return response.json()["response"].strip()
    except httpx.ReadTimeout:
        print("Request timed out. The server is taking too long to respond.")
        return "Error: Request timed out."
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return "Error: An HTTP error occurred."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error: An unexpected error occurred."

def explain_selection():
    # Copy selection to clipboard
    with controller.pressed(Key.cmd):
        controller.tap("c")
    time.sleep(0.1)  # Wait for the clipboard to update
    error_text = pyperclip.paste()

    if not error_text:
        messagebox.showinfo("Info", "No text selected.")
        return

    explanation = explain_error(error_text)
    if not explanation:
        messagebox.showerror("Error", "Failed to get an explanation.")
        return

    messagebox.showinfo("Error Explanation", explanation)

def on_activate_explain():
    explain_selection()

# Running the listener in a separate thread to avoid blocking tkinter's main loop
def start_listener():
    with keyboard.GlobalHotKeys({
        "<ctrl>+<cmd>+e": on_activate_explain
    }) as h:
        h.join()

listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

# Start the tkinter event loop
root.mainloop()


