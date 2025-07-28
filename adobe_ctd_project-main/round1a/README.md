# 📘 Connecting the Dots – Round 1A: PDF Outline Extractor

## ✨ Challenge Overview

The goal of Round 1A is to transform static PDFs into structured, intelligent outlines by extracting:
- Title
- Section headings (H1, H2, H3)
- Page numbers

This outline will form the base for Round 1B's intelligent document interaction system.

---

## 🔍 What the Solution Does

This solution:
- Accepts any PDF file from the `/app/input/` directory (up to 50 pages)
- Extracts the **document title** and all heading-level text (H1, H2, H3)
- Outputs a well-formatted `filename.json` to `/app/output/` in the required format

---

## 📦 Libraries Used

- `pdfplumber`: For precise layout-based PDF text extraction
- `PyMuPDF (fitz)`: (Optional) for layout understanding
- `json`: To generate output file
- `os`: For directory handling

---

## 🧠 Approach

1. **Font Size Analysis**:
   - Parse every word in the document
   - Track the top 3 most frequent font sizes
   - Use those sizes to infer heading levels (H1, H2, H3)

2. **Title Detection**:
   - The first occurrence of the largest font size is assumed to be the title

3. **Heading Extraction**:
   - All words matching the top 3 sizes are collected as potential H1–H3
   - Stored with level, text, and page number

4. **Output**:
   - JSON file with `title` and structured `outline` list

---

## 🐳 How to Build and Run (for Reviewers)

### Build the Docker Image

```bash
docker build --platform linux/amd64 -t dotreader:vasu-v1 .
