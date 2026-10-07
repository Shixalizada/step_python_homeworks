import lesson2_hw
import lesson3_hw
import lesson4_hw


def menu():
    while True:
        print("\nSTEP IT Academy - Python Homework Project")
        print("1 - Dərs 2 testlərini işə sal")
        print("2 - Dərs 3 testlərini işə sal")
        print("3 - Dərs 4 testlərini işə sal")
        print("0 - Çıxış")

        secim = input("Seçim: ")

        if secim == "1":
            exec(open("lesson2_hw.py", encoding="utf-8").read())
        elif secim == "2":
            exec(open("lesson3_hw.py", encoding="utf-8").read())
        elif secim == "3":
            exec(open("lesson4_hw.py", encoding="utf-8").read())
        elif secim == "0":
            print("Proqram bağlandı.")
            break
        else:
            print("Yanlış seçim.")


if __name__ == "__main__":
    menu()
