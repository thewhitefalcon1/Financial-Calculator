'''
Модуль, содержащий основные функции для финансовых вычислений
'''
import numpy as np
import numpy_financial as npf


#функции для процентов

def simple_interest(principal: float, rate: float, years: float) -> float:

    """
    Функция реализующая простые проценты.
    principal: начальная сумма
    rate: годовая ставка (например, 0.05 = 5%)
    years: срок в годах
    """
    return principal * rate * years

def compound_interest(principal: float, rate: float, times_compounded: int, years: float) -> float:
    """
    Сложные проценты.
    principal: начальная сумма
    rate: годовая ставка
    times_compounded: сколько раз начисляются проценты в год
    years: срок в годах
    """
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return round(amount, 2)

#функция для кредита

def loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """
    Рассчитывает ежемесячный платёж по аннуитетному кредиту.
    principal: сумма кредита
    annual_rate: годовая процентная ставка (например, 0.12 = 12%)
    years: срок кредита в годах
    """
    monthly_rate = annual_rate / 12
    n_months = years * 12
    payment = npf.pmt(monthly_rate, n_months, -principal)
    return round(payment, 2)


#инвестиционные функции

def roi(gain: float, cost: float) -> float:
    """
    Возвращает окупаемость инвестиций (ROI) в процентах.
    gain: прибыль (итоговая сумма)
    cost: затраты
    """
    return round((gain - cost) / cost * 100, 2)


def npv(rate: float, cash_flows: list[float]) -> float:
    """
    Чистая приведённая стоимость (Net Present Value).
    rate: ставка дисконтирования (например, 0.1 = 10%)
    cash_flows: список денежных потоков (первый элемент - инвестиция со знаком минус)
    """
    return round(npf.npv(rate, cash_flows), 2)


def irr(cash_flows: list[float]) -> float:
    """
    Внутренняя норма доходности (Internal Rate of Return).
    cash_flows: список денежных потоков
    """
    return round(npf.irr(cash_flows) * 100, 2)


