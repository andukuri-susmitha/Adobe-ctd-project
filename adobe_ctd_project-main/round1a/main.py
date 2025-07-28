import os
import json
from extractor import extract_outline_from_pdf

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

            try:
                title, outline = extract_outline_from_pdf(pdf_path)
                output = {
                    "title": title,
                    "outline": outline
                }
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(output, f, indent=2)
                print(f"[✓] Processed {filename}")
            except Exception as e:
                print(f"[x] Failed to process {filename}: {e}")

if __name__ == "__main__":
    main()
