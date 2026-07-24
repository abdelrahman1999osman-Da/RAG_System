import fitz

from config.settings import settings
from config.chapters import CHAPTERS_CONFIG

fitz.TOOLS.mupdf_display_errors(False)


class PDFLoader:

    def __init__(self):
        self.pdf_path = settings.PDF_PATH

    def load(self):

        doc = fitz.open(self.pdf_path)

        chapters = []

        for idx, chapter in enumerate(CHAPTERS_CONFIG, start=1):

            text = ""

            start_page = chapter["start"] - 1
            end_page = chapter["end"]

            for page_num in range(start_page, end_page):

                if page_num < len(doc):
                    text += doc[page_num].get_text() + "\n"

            chapters.append({
                "document_id": idx,
                "title": chapter["title"],
                "page_start": chapter["start"],
                "page_end": chapter["end"],
                "text": text.strip()
            })

        doc.close()

        return chapters