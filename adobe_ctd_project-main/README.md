🧠 Adobe Hackathon: Connecting the Dots – Round 1A & 1B Submission
Welcome to our submission for the Adobe Hackathon - Connecting the Dots Challenge. This project contains solutions for both Round 1A (Structured Outline Extraction) and Round 1B (Intelligent Document Analyst System).

📁 Project Structure
css
Copy
Edit
adobe_ctd_project/
├── round1a/                    ← PDF Outline Extraction System
│   ├── input/                 ← Raw PDF files
│   ├── output/                ← Extracted structured outlines (JSON)
│   ├── main.py
│   ├── extractor.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── round1b/                    ← Intelligent Document Analyst System
│   ├── data/                  ← Sample documents and labeled data
│   ├── model/                 ← ML/NLP models (if applicable)
│   ├── src/
│   │   ├── app.py             ← Main logic/backend/API
│   │   └── utils.py           ← Helper functions
│   ├── templates/             ← HTML templates (for UI, optional)
│   ├── static/                ← CSS, JS files (if applicable)
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
└── Combined_README.md         ← This file
🧩 Round 1A – Structured Outline Extraction
✅ Objective
To extract a hierarchical structure (H1, H2, H3) from a PDF document and output it as a JSON object, capturing the document’s outline.

🛠️ Technologies Used
Python

PyMuPDF / pdfminer.six

JSON

Docker

🚀 How to Run (Round 1A)
bash
Copy
Edit
cd round1a/
pip install -r requirements.txt
python main.py input/sample.pdf output/sample.json
🤖 Round 1B – Intelligent Document Analyst
✅ Objective
To build a system that performs semantic-level analysis on a document. This may include:

Content classification

Summarization

Keyword extraction

Custom insights for different document types

🧠 Techniques Used
NLP using SpaCy / HuggingFace Transformers

Rule-based or model-based classification

REST API using Flask (optional UI)

🛠️ Technologies Used
Python

Flask (optional)

NLTK / SpaCy / Transformers

HTML/CSS (for UI)

Docker

🚀 How to Run (Round 1B)
bash
Copy
Edit
cd round1b/
pip install -r requirements.txt
python src/app.py
📌 Notes
Please check the individual README.md inside each round folder for detailed instructions.

All code is modular, clean, and adheres to best practices.

Test files are provided in the input/ and data/ directories.

👩‍💻 Contributors
Vasudha Jogi
Email: vasudhajogi@gmail.com

GitHub: vasudhajogi20

LinkedIn: Vasudha Jogi

Susmitha Andukuri
Email: andhukurisusmitha@gmail.com

GitHub: andukuri-susmitha

LinkedIn: Susmitha Andukuri

📬 Contact & Questions
For any queries regarding the project, feel free to connect via email or LinkedIn.
Thank you for this opportunity! 🙌