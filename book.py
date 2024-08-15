import fitz

def format_text(text):
    lines = text.splitlines()  
    formatted_text = []
    previous_line = ""
    
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            if previous_line and previous_line[-1] != '.':
                formatted_text[-1] += " " + stripped_line
            else:
                formatted_text.append(stripped_line)
        else:
            formatted_text.append("")
        previous_line = stripped_line

    return "\n\n".join(formatted_text)

def pdf_text(book):
    pdf = fitz.open("book/" + book)

    text = ""
    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        text += page.get_text()

    pdf.close()
    formatted_text = format_text(text)

    with open("book/book.txt", "w", encoding="utf-8") as file:
        file.write(formatted_text)
    
    return
