import os
from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LLAMA_CLOUD_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please set LLAMA_CLOUD_API_KEY in your .env file")

parser = LlamaParse(
    api_key=api_key, 
    result_type="markdown", 
    parse_mode="parse_page_with_llm", 
    verbose=True,
)

pdf_path = "./your_document.pdf"  # <--- REPLACE THIS WITH YOUR FILE

file_name_without_ext = os.path.splitext(os.path.basename(pdf_path))[0]
output_path = f"projects/{file_name_without_ext}.md"


print("Parsing document... this may take a moment.")
documents = parser.load_data(pdf_path)

full_text = documents[0].text

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Success! Markdown saved to {output_path}")

print("\n--- Preview ---")
print(full_text[:500])