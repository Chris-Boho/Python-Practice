#!/usr/bin/python3

# import googletrans
from googletrans import Translator
from deep_translator import MyMemoryTranslator, LingueeTranslator, PonsTranslator
from numpy import source


def main():
    # print(googletrans.LANGUAGES)

    toTranslate = input('Enter text to be translated: ')

    gTranslator = Translator()
    result = gTranslator.translate(toTranslate)

    print('src: ' + result.src)
    print('dest: ' + result.dest)
    print('origin: ' + result.origin)
    print('------TRANSLATIONS------')
    print('Google_Text: ' + result.text)

    myMemTranslator = MyMemoryTranslator(source=result.src, target='english').translate(toTranslate)

    print('MyMem_Text: ' + myMemTranslator)

    # lingTranslator = LingueeTranslator(source=result.src, target='english').translate(toTranslate)
    # print('Linguee_Text: ' + lingTranslator)

    ponsTrans = PonsTranslator(source=result.src, target='english').translate(toTranslate)
    print('Pons_Text: ' + ponsTrans)


if __name__ == '__main__':
    main()
