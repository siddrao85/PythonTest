import pyttsx3
import PyPDF2

# Replace 'file.pdf' with path to your PDF file (i.e. /Desktop/Contracts/file.pdf)
pdf_path = '/Users/siddh/Desktop/Espresso.pdf'

# Open the PDF file
with open(pdf_path, 'rb') as file:
    pdfreader = PyPDF2.PdfReader(file)

    reader = pyttsx3.init()
    full_text = ""

    for page in range(len(pdfreader.pages)):
        text = pdfreader.pages[page].extract_text()
        legible_text = text.strip().replace('\n', ' ')
        print(legible_text)
        full_text += legible_text + " "
        reader.say(legible_text)
        reader.runAndWait()

    # Save the entire text to an audio file
    reader.save_to_file(full_text, 'espresso.mp3')
    reader.runAndWait()

reader.stop()