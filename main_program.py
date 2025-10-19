
from calc_functions import *
1
def main():
    while True:
        print()
        print("      ФИНАНСОВЫЙ КАЛЬКУЛЯТОР ")
        print()
        print("Список возможных операций")
        print()
        print("1. Простые проценты")
        print("2. Сложные проценты")
        print("3. Кредитный платёж")
        print("4. ROI (окупаемость инвестиций)")
        print("5. NPV (чистая приведённая стоимость)")
        print("6. IRR (внутренняя норма доходности)")
        print("0. Выход")
        print()

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            p = float(input("Введите сумму (principal): "))
            r = float(input("Введите ставку (например, 0.05 для 5%): "))
            t = float(input("Введите срок в годах: "))
            print(f"Простые проценты: {simple_interest(p, r, t):.2f}")

        elif choice == "2":
            p = float(input("Введите сумму (principal): "))
            r = float(input("Введите ставку (например, 0.05 для 5%): "))
            n = int(input("Сколько раз начисляются проценты в год (например, 4): "))
            t = float(input("Введите срок в годах: "))
            print(f"Сложные проценты: {compound_interest(p, r, n, t):.2f}")

        elif choice == "3":
            p = float(input("Введите сумму кредита: "))
            r = float(input("Введите годовую ставку (например, 0.12): "))
            y = int(input("Введите срок кредита в годах: "))
            print(f"Ежемесячный платёж: {loan_payment(p, r, y):.2f}")

        elif choice == "4":
            gain = float(input("Введите прибыль (gain): "))
            cost = float(input("Введите затраты (cost): "))
            print(f"ROI: {roi(gain, cost):.2f}%")

        elif choice == "5":
            rate = float(input("Введите ставку дисконтирования (например, 0.1): "))
            n = int(input("Введите количество периодов: "))
            flows = []
            for i in range(n):
                flow = float(input(f"Поток {i+1}: "))
                flows.append(flow)
            print(f"NPV: {npv(rate, flows):.2f}")

        elif choice == "6":
            n = int(input("Введите количество потоков: "))
            flows = []
            for i in range(n):
                flow = float(input(f"Поток {i+1}: "))
                flows.append(flow)
            print(f"IRR: {irr(flows):.2f}%")

        elif choice == "0":
            print("До свидания ")
            break

        else:
            print("Ошибка: выберите пункт из списка (0–6).")


if __name__ == "__main__":
    main()