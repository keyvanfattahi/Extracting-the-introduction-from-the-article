import re
import PyPDF2

def extract_abstract(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        abstract_text = ""
        abstract_found = False

        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()

            # بررسی بخش Abstract
            if "Abstract" in page_text or "ABSTRACT" in page_text or "A B S T R A C T" in page_text or  "چکیده" in page_text or  "1.چکیده" in page_text or  "1 چکیده" in page_text:
                abstract_found = True
                abstract_start = page_text.lower().index("abstract")

                # بررسی هر کدام از بخش‌های مورد نظر
                if "1 introduction" in page_text.lower():
                    abstract_end = page_text.lower().find("1 introduction")
                elif "introduction" in page_text.lower():
                    abstract_end = page_text.lower().find("introduction")
                elif "Introduction" in page_text:
                    abstract_end = page_text.lower().find("Introduction")
                elif "1 Introduction" in page_text:
                    abstract_end = page_text.lower().find("1 Introduction")
                elif "1Introduction" in page_text:
                    abstract_end = page_text.lower().find("1Introduction")
                elif "1introduction" in page_text:
                    abstract_end = page_text.lower().find("1introduction")
                elif "مقدمه" in page_text:
                    abstract_end = page_text.lower().find("مقدمه")
                else:
                    abstract_end = len(page_text)

                abstract_text += page_text[abstract_start:abstract_end]


        if abstract_found:
            print("متن بخش Abstract:")
            print(abstract_text)
            save_as_html(pdf_file, abstract_text.rstrip("1"))
        else:
            print("بخش Abstract یافت نشد.")

def save_as_html(pdf_file, abstract_text):
    file_name = input("نام فایل HTML را وارد کنید: ")
    file_name = file_name.strip()
    if not file_name.endswith(".html"):
        file_name += ".html"

    # حذف کلمه "abstract" از ابتدای متن
    abstract_text = re.sub(r'^\s*abstract\s*', '', abstract_text, flags=re.IGNORECASE)

    with open(file_name, 'w', encoding='utf-8') as file:
        html_content = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Abstract</title>
        </head>
        <body>
            <h1>متن بخش Abstract</h1>
            <p>{abstract_text}</p>
        </body>
        </html>
        '''
        file.write(html_content)

        print(f"فایل HTML با نام '{file_name}' ذخیره شد.")

# بخشی برای گرفتن آدرس فایل pdf
pdf_file_path = input("نام فایل PDF را وارد کنید: ")
pdf_file_path = pdf_file_path.strip()
extract_abstract(pdf_file_path)
