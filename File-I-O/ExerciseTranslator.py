# run pip install translate

from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('./data/oopf.text', mode='r') as trfile:
        text = trfile.read()
        print(text)
        translation = translator.translate(text)
        print(translation)
        with open('./data/oopf-ja.text', mode='w', encoding="utf-8") as trfile2:
            trfile2.write(translation)
except FileNotFoundError as err:
    print('File does not exit :(')
    raise  err


