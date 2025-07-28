import pdfplumber

def extract_outline_from_pdf(pdf_path):
    headings = []
    title = None
    with pdfplumber.open(pdf_path) as pdf:
        font_counts = {}
        for page_no, page in enumerate(pdf.pages, 1):
            for w in page.extract_words(extra_attrs=["size", "fontname"]):
                sz = round(w["size"], 1)
                font_counts[sz] = font_counts.get(sz, 0) + 1

        top_sizes = sorted(font_counts, key=lambda s: -font_counts[s])[:3]
        max_sz, mid_sz, min_sz = (top_sizes + [None]*3)[:3]

        for page_no, page in enumerate(pdf.pages, 1):
            for w in page.extract_words(extra_attrs=["size", "fontname"]):
                sz = round(w["size"], 1)
                txt = w["text"].strip()
                if sz == max_sz:
                    if title is None:
                        title = txt
                    else:
                        headings.append({"level": "H1", "text": txt, "page": page_no})
                elif sz == mid_sz:
                    headings.append({"level": "H2", "text": txt, "page": page_no})
                elif sz == min_sz:
                    headings.append({"level": "H3", "text": txt, "page": page_no})

    return title or "Untitled Document", headings
