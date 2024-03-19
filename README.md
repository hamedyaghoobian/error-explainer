# Code Explainer: An Error Explanation Assistant

A Python script designed to run in the background, listening for specific hotkeys. When triggered, it uses the OLLAMA Large Language Model to explain coding errors in the selected text, displaying the explanations in a sleek, macOS lookup-style popup. This utility, consisting of less than 100 lines of code, enhances coding efficiency by providing instant, in-context explanations of errors directly within your text editor or IDE.

This project extends the concept by leveraging AI not just for corrections but for providing insights into coding mistakes, facilitating a faster and more informed coding process.

## Getting Started

### 1. Set up OLLAMA

First, ensure you have OLLAMA installed and running on your system. OLLAMA is an AI model server that can be easily set up and queried for various tasks, including explaining coding errors.

Installation guide for OLLAMA: https://github.com/ollama/ollama

Start the model suitable for explaining code:
```
ollama run codellama
```

While the Mistral 7B Instruct model is recommended for its adeptness at explaining code, feel free to explore and utilize other models that OLLAMA supports.

### 2. Install Required Dependencies

Ensure the following Python libraries are installed to use the script effectively:

```
pip install pynput pyperclip httpx tkinter
```

- **pynput**: For monitoring and controlling the keyboard. [Documentation](https://pynput.readthedocs.io/en/latest/)
- **pyperclip**: For accessing and modifying the system clipboard. [GitHub](https://github.com/asweigart/pyperclip)
- **httpx**: A fully featured HTTP client for Python 3. [Documentation](https://www.python-httpx.org/)
- **tkinter**: Python's de-facto standard GUI (Graphical User Interface) package.

### 3. Run the Assistant

Execute the script to start the typing assistant:

```
python main.py
```

**Hotkeys to trigger explanations:**

- `Ctrl+Cmd+e`: Explain the error in the current selection.

Ensure you select the piece of code with a potential error before pressing the hotkey.

**Note**: This script is tailored for macOS. Key bindings such as `Key.cmd` might require adjustments for compatibility with other operating systems, e.g., changing to `Key.ctrl` for Windows or Linux environments.

## Customization

The script offers flexible customization options, including hotkeys, prompt templates, and OLLAMA configuration, to suit your preferences and needs.

### Example Prompt Templates

Customize your prompts to OLLAMA for different tasks. Here are some examples you might find useful:

```python
from string import Template

# Template for explaining coding errors
PROMPT_TEMPLATE_EXPLAIN_ERROR = Template(
    """Explain the following coding error in detail:

$error
"""
)

# Template for generating text based on a topic
PROMPT_TEMPLATE_GENERATE_TEXT = Template(
    """Generate a paragraph about the following topic, incorporating humor and insight:

$text
"""
)

# Template for summarizing text
PROMPT_TEMPLATE_SUMMARIZE_TEXT = Template(
    """Summarize the following text in a concise and informative manner:

$text
"""
)
```

Adapt and expand these templates as needed to harness the full potential of the OLLAMA model for your coding and writing tasks.