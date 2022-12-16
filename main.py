from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path: str, language: str = 'en') -> str:
    """
    Convert PDF file to mp3 function.
    Takes PDF file path and language
    :param file_path: (str) Directory path with PDF file
    :param language: (str) Language code, used for audio text transform
    :return: (str) .mp3 file will be added to base directory if file is correct.
    In other way, unsuccessful message will be sent.
    """
    if not Path(file_path).exists() and Path(file_path).suffix == '.pdf':
        return 'PDF file was not found.'

    with pdfplumber.open(file_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    text = ''.join(pages).replace('\n', '')

    my_audio = gTTS(text=text, lang=language, slow=False)
    my_audio.save(f'{Path(file_path).stem}.mp3')

    return 'Mp3 file with {} text was successfully saved'.format(Path(file_path).stem)


def main() -> None:
    """
    Main function to start the pdf_to_mp3 func.
    """
    file_path = input('Input your pdf file path: ')
    language = input('Input language code: ')
    pdf_to_mp3(file_path=file_path, language=language)


if __name__ == '__main__':
    main()
