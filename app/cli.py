import sys
from models import add_expense, list_expenses

def show_menu():
    print("\nExpense Tracker - CLI")
    print("1. Gider Ekle")
    print("2. Giderleri Listele")
    print("3. Çıkış")

def main():
    while True:
        show_menu()
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            date = input("Tarih (YYYY-MM-DD): ")
            category = input("Kategori: ")
            amount = float(input("Tutar: "))
            description = input("Açıklama: ")
            add_expense(date, category, amount, description)
            print("[✔] Gider başarıyla eklendi.")
        elif choice == "2":
            expenses = list_expenses()
            print("\n--- Giderler ---")
            for exp in expenses:
                print(f"{exp[1]} | {exp[2]} | {exp[3]} TL | {exp[4]}")
        elif choice == "3":
            print("Çıkış yapılıyor...")
            sys.exit()
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
