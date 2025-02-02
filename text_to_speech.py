from gtts import gTTS
import os
import platform

class TextToSpeech:
    def __init__(self, text, lang='en', slow=False):
        self.text = text
        self.lang = lang
        self.slow = slow
        self.tts = gTTS(text=self.text, lang=self.lang, slow=self.slow)

    def save(self, filename):
        self.tts.save(filename)

    def play(self, filename):
        if platform.system() == "Windows":
            os.system(f"start {filename}")
        elif platform.system() == "Darwin":  # menda macOS ammo windows va linuxda ishlashi uchun shu if else bloklarini qo'shdim
            os.system(f"afplay {filename}")
        else:
            os.system(f"aplay {filename}")

    @staticmethod
    def from_file(file_path, lang='en', slow=False):
        with open(file_path, 'r') as file:
            text = file.read()
        return TextToSpeech(text, lang, slow)


if __name__ == "__main__":
    root_path = "audio/"

    #oddiy matnni ovozga aylantirish
    about_me = TextToSpeech("Hi, I am John. I am a software developer.")
    about_me.save(f"{root_path}about_me.mp3")
    about_me.play(f"{root_path}about_me.mp3")

    # ingliz tilida matnni ovozga aylantirish
    file_data = TextToSpeech.from_file("texts/text_en.txt")
    file_data.save(f"{root_path}text_en.mp3")
    # file_data.play(f"{root_path}text_en.mp3")

    # rus tilida matnni ovozga aylantirish
    file_data = TextToSpeech.from_file("texts/text_ru.txt", lang='ru')
    file_data.save(f"{root_path}text_ru.mp3")
    file_data.play(f"{root_path}text_ru.mp3")
