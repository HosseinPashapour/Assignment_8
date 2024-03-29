print (" TRANSLATOR ")
import gtts
import os

jomle = ''
def show_menu():
    print('======================')
    print('Welcome to my translator')
    print('1- Translate english to persian')
    print('2- Translate persian to english')
    print('3- Add new word to dictionary')
    print('4- Exit')
    print('======================')

def read_from_file():
    global words_bank
    result = os.listdir('../Assignment-8')
    if 'translate.txt' in result:
        f = open('translate.txt','r')
        temp = f.read().split('\n')
        words_bank = []
        for i in range(0, len(temp)-1, 2):
            my_dict = {"en":temp[i], "fa":temp[i+1]}
            words_bank.append(my_dict) 
        f.close()
        return words_bank
    else:
        print('No word bank found...!')


def translate_english_to_persian():
    global jomle
    user_text = input("Enter your english text: ")
    user_words = user_text.split(' ')
    for user_word in user_words:
        for word in words_bank:
            if user_word == word['en']:
                jomle = jomle + word['fa'] + ' ' 
                break
        else:
                jomle = jomle + user_word + ' ' 
    return jomle

def translate_persian_to_english():
    global jomle
    user_text = input("Enter your persian text: ")
    user_words = user_text.split(' ')

    for user_word in user_words:
        for word in words_bank:
            if user_word == word['fa']:
                jomle = jomle + word['en'] + ' ' 
                break
        else:
            jomle = jomle + user_word + ' ' 
    return jomle

def add_new_word(en_word:str, fa_word:str):
    file = open('translate.txt','a')
    file.write('\n')
    file.write(en_word + '\n')
    file.write(fa_word + '\n')
    file.close()

read_from_file()

while True:
    show_menu()
    choice = int(input('enter your choice: '))
    
    if choice == 1:
        translate_english_to_persian()
        print(jomle)
        translate_sound = gtts.gTTS(jomle, lang='ar')
        translate_sound.save('translate_to_persian.mp3')
        jomle = ''
    elif choice ==2:
        translate_persian_to_english()
        print(jomle)
        translate_sound = gtts.gTTS(jomle, lang='en')
        translate_sound.save('translate_to_english.mp3')
        jomle = ''
    elif choice ==3:
        en = input('Enter english word: ')
        fa = input('Enter farsi word: ')
        add_new_word(en,fa)
        print('New word added successfully...')
    elif choice ==4:
        exit(0)