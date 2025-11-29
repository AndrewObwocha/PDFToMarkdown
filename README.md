# PDF to LLM-Ready Markdown Converter

A robust Python utility designed to convert PDF documents into structured Markdown. This tool is specifically optimized for **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)** pipelines.

> **The Problem:** Standard PDF extraction often results in a "soup" of text where headers, footers, and table rows get jumbled.
>
> **The Solution:** This tool uses **LlamaParse** (State-of-the-Art) to "see" the document layout, preserving tables, headers, and structural hierarchy so your AI can understand the content accurately.

## 🚀 Key Features

- **Structure Preservation:** accurately converts complex tables, multi-column layouts, and charts into Markdown format.
- **Dynamic Output Naming:** Automatically extracts the filename from the input and saves the output with the same name (e.g., `Annual_Report.pdf` → `Annual_Report.md`).
- **Cost-Optimized:** Pre-configured to use "Balanced Mode" (~3 credits/page), offering high accuracy without the high cost of premium GPT-4o parsing.
- **Secure:** Uses environment variables (`.env`) to keep API keys out of your source code.

## 🛠️ Prerequisites

1.  **Python 3.8+** installed.
2.  A **LlamaCloud API Key**.
    - Get one for free at [cloud.llamaindex.ai](https://cloud.llamaindex.ai).
    - _Note: The free tier currently includes ~1000 pages/day via their monthly credit system._

## 📦 Installation

1.  **Clone the repository** (or download the files):

    ```bash
    git clone https://github.com/YourUsername/Your-Repo-Name.git
    cd Your-Repo-Name
    ```

2.  **Create and Activate a Virtual Environment** (Recommended):

    ```bash
    # Windows
    python -m venv myenv
    myenv\Scripts\activate

    # Mac/Linux
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install llama-parse python-dotenv
    ```

## ⚙️ Configuration

1.  Create a file named `.env` in the root directory.
2.  Add your API key to the file:
    ```text
    LLAMA_CLOUD_API_KEY=llx-xxxxxxxxxxxxxxxxxxxxxxxx
    ```
    _(Note: Do not commit this file to GitHub. It is already added to .gitignore if you initialized one)._

## 🏃 usage

1.  Open `parser.py` and modify the `pdf_path` variable to point to your target PDF:

    ```python
    pdf_path = "./reports/my_complex_document.pdf"
    ```

2.  Run the script:

    ```bash
    python parser.py
    ```

3.  **Check the output:**
    The script will generate a `.md` file in the same directory (or specified output path) containing the structured text.

## 💡 How it Works

The script utilizes the `LlamaParse` library with the following specific configuration:

- **`result_type="markdown"`**: Forces the output into Markdown syntax (headers as `#`, tables as `| col | col |`).
- **`parse_mode="parse_page_with_llm"`**: Uses a lightweight LLM to reconstruct the layout (Balanced Mode).

## 📄 License

[MIT License](LICENSE)
