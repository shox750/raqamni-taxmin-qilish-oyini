import nomalum_son

def raqam_taxmin_qilish_oyini():
    print("Sonni top o'yiniga xush kelibsiz")

    pastki_chegara = int(input("Oraliqning pastki chegarasini kiriting: "))
    yuqori_chegara = int(input("Oraliqning yuqori chegarasini kiriting: "))

    # random son yaratadigan funksiya
    random_son = nomalum_son.random_son_genetarsiya(pastki_chegara, yuqori_chegara)

    urinishlar = 0

    #print(random_son)  # Test uchun

    while True:
        foydalanuvchi_kiritadigan_son = int(input("Taxminiy son kiriting: "))
        urinishlar += 1

        if foydalanuvchi_kiritadigan_son > random_son:
            print("Siz kiritgan son, nomalum sondan katta.")
        elif foydalanuvchi_kiritadigan_son < random_son:
            print("Siz kiritgan son, nomaum sondan kichik.")
        else:
            print(f"\n-----------------\nTabriklaymiz! Siz {urinishlar} ta urinishda nomalum sonni topdingiz!\nNomalum son: {random_son}")
            break

    print("O'yin tugadi.")

# O'yin boshlanadigan funksiya (start)
raqam_taxmin_qilish_oyini()