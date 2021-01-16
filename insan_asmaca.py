# Problem Set 2, insan_asmaca.py
# İsim: Esmanur Karaca
# Katkıda bulunanlar Kelim Almusa:
# Harcanan Zaman:


import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'


def kelimeleri_yükle():

    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower()
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı. \n")
    return kelime_listesi


def kelime_seç(kelime_listesi):

    return random.choice(kelime_listesi)


kelime_listesi = kelimeleri_yükle()


def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    for x in tahmin_edilen_harfler:
        if(gizli_kelime.find(x) == -1):
            return False
        if(len(gizli_kelime) != len(tahmin_edilen_harfler)):
            return False
        return True
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime;
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi;
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri tahmin_edilen_harfler içindeyse True;
        aksi takdirde False
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN

    return


def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime;
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi;
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime içindeki hangi harflerin
        şimdiye kadar tahmin edildiğini temsil eden boşluklardan oluşur.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass


def uygun_harfleri_al(tahmin_edilen_harfler, alfabe=TÜRKÇE_ALFABE):
     for char in tahmin_edilen_harfler:
            TÜRKÇE_ALFABE = TÜRKÇE_ALFABE.replace(char, "")
    return TÜRKÇE_ALFABE
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
        eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    pass


def insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    print("İnsan asmaca oyununa hoş geldiniz !")
    print("6 hakkınız var")
    print("%d harfli bir kelime düşünüyorum " % (len(gizli_kelime)))
    word_display = ('-') * len(gizli_kelime)

    print("uygun harfler :" + alfabe)
    print(word_display + "\n")

    # liste[0]=alfabe
    guessed = False
    guessed_letters = []  # tahminde bulunulan harfler ve kelimeler
    guessed_word = []
    tries = 6
    count = 0
    uyari = 3
    unlu = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    dogru_harf = 0
    flag = 0
    while not guessed and tries > 0:

        if count == 1:
            print("uygun harfler :" + alfabe)
        guess = input("Bir tahminde bulununuz").lower()

        count = 1

        if len(guess) == 1 and guess.isalpha():  # tahmin guess latter içinde varsa

            if guess in guessed_letters:
                if uyari == 0:
                    tries -= 1
                    print("%s harfini daha önce denediniz  %d  hakkınız kaldı" % (
                        guess, tries))
                else:
                    uyari -= 1
                    print("%s harfini daha önce denediniz  %d uyarı hakkınız kaldı" % (
                        guess, uyari))
                    print("Uygun harfler %s:" % (alfabe))

            elif guess not in gizli_kelime:  # if else elif e dikkat
                if guess in unlu:
                    tries -= 2
                else:
                    tries -= 1
                print("Oops! %s bu harf benim kelimemde yok :  %s " %
                      (guess, word_display))
                print("%d hakkınız kaldı " % (tries))
                guessed_letters.append(guess)
                if guess in alfabe:
                    for i in alfabe:
                        if i == guess:
                            alfabe = alfabe.replace(i, "")
                print("Uygun harfler :" + str(alfabe))

            else:
                print("%s harfi kelimede var " % (guess))
                dogru_harf += 1
                guessed_letters.append(guess)
                # harf doğru ise indexlerde gösterme
                word_as_array = list(word_display)
                indices = [i for i, letter in enumerate(
                    gizli_kelime) if letter == guess]
                # for index in indices:
                # word_as_array[index] = guess
                word_as_array = [
                    letter if letter in guessed_letters else '-' for letter in gizli_kelime]
                word_display = ' '.join(word_as_array)
                if "-" not in word_display:
                    guessed = True
                elif guess in alfabe:
                    for i in alfabe:
                        if i == guess:
                            alfabe = alfabe.replace(i, "")
            count = 1
        elif len(guess) == len(gizli_kelime) and guess.isalpha():  # harf kelimede yoksa
            if guess == gizli_kelime:
                guessed = True
                word_display = gizli_kelime
            else:
                print("Doğru değil")
                guessed_word.append(guess)
                tries -= 1
            count = 1
        elif len(guess) == 1 and guess == "*":
            olası_eşleşmeleri_göster(word_display)
            print("Oyundan çıkılıyor...")
            flag = 1
            break
        else:
            if uyari == 0:
                tries -= 1
                print("Oops! Bu geçerli bir harf değil  %d hakkınız kaldı :  %s" % (
                    tries, word_display))
            else:
                uyari -= 1
                print("Oops! Bu geçerli bir harf değil. %d uyarı hakkınız kaldı  :  %s" % (
                    uyari, word_display))

            count = 1
        print(word_display + "\n")  # her tahminde sonra word ü göstermen lazım
        print("%d tahmin hakkınız kaldı " % (tries))
    if guessed:
        print("Tebrikler . Kazandınız..")
        print("Puanınız %d :" % (dogru_harf*tries))
    elif guessed == False and flag == 0:
        print("Malesef hakkınız bitti. Doğru cevap : %s" % (gizli_kelime))


def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):

    if benim_kelimem == diğer_kelime or len(benim_kelimem) == len(diğer_kelime):
        return True
    else:
        False


def olası_eşleşmeleri_göster(benim_kelimem):

    indices = [i for i, letter in enumerate(benim_kelimem) if letter != "_"]
    list = []

    for kelime in kelime_listesi:
        count = 0
        if len(benim_kelimem) == len(kelime):

            for index in range(0, len(benim_kelimem)):

                if index in indices:
                    if benim_kelimem[index] == kelime[index]:
                        count += 1
            if count == len(indices):
                list.append(kelime)

    if len(list) != 0:
        for i in list:
            print(i)
    else:
        print("Eşleşme bulunamadı...")


def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):

    insan_asmaca(gizli_kelime, alfabe)


if __name__ == "__main__":
    # pass
    # insan_asmaca("abadan","abcçdefghıjkştryvzmn")
    word = kelime_seç(kelime_listesi)
    ipuçlarıyla_insan_asmaca(word, TÜRKÇE_ALFABE)
    # Bölüm 2'yi test etmet için, yukarıdaki "pass" satırına yorum işaretini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.

    # gizli_kelime = kelime_seç(kelime_listesi)
    # insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)
    # olası_eşleşmeleri_göster("_e___a")
###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    # Bölüm 3'ü test etmek için yukarıdaki satırlara yeniden yorum işaretlerini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.

    # gizli_kelime = kelime_seç(kelime_listesi)
    # ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)
