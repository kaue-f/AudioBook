import pyttsx3

def book_audio(title):
    engine = pyttsx3.init()

    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(f"ID: {voice.id}")
    #     print(f"Name: {voice.name}")
    #     print(f"Language: {voice.languages}")
    #     print(f"Gender: {voice.gender}")
    #     print("-" * 30)

    with open('book/book.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
    engine.save_to_file(text, 'audio/'+ title +'.mp3')
    engine.runAndWait()
    if os.path.exists("book/book.txt"):
        os.remove("book/book.txt")
    return