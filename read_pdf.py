import sys
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("No PyPDF2 or pypdf found")
        sys.exit(1)

pdf_path = r"C:\Users\guiva\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\1AA1A777A920A2D3DD012FD39926A8BD844C53FD\transfers\2026-08\roteiro versão 1.0 final.pdf"

try:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open('pdf_output.txt', 'w', encoding='utf-8') as f:
        f.write(text)
except Exception as e:
    with open('pdf_output.txt', 'w', encoding='utf-8') as f:
        f.write(f"Error: {e}")
