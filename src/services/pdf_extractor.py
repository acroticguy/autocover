import fitz  # PyMuPDF
from typing import Tuple


def extract_text_from_pdf(pdf_bytes: bytes) -> Tuple[str, bool]:
    """
    Extract text from PDF bytes.

    Returns:
        Tuple of (extracted_text, success)
    """
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text_blocks = []

        for page in doc:
            text = page.get_text("text")
            if text.strip():
                text_blocks.append(text)

        doc.close()

        if not text_blocks:
            return "", False

        return "\n\n".join(text_blocks), True

    except Exception as e:
        return f"Error extracting PDF: {str(e)}", False
