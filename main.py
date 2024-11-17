from dataclasses import dataclass
from datetime import date
from typing import List

NUM_RESIDENTS = 4
MESSAGE_FORMAT = "Total: ${:.2f} (or ${:.2f} per person)"


@dataclass
class Bill:
    start: date
    end: date
    amount: float


def get_days_in_month(year: int, month: int) -> int:
    curr_month_start = date(year, month, 1)
    if month < 12:
        next_month_start = date(year, month + 1, 1)
    else:
        next_month_start = date(year + 1, month, 1)
    return (next_month_start - curr_month_start).days - 1


def get_month_start_for_bill(bill: Bill, month: int) -> date:
    if month == bill.start.month:
        return bill.start
    return date(bill.start.year, month, 1)


def get_month_end_for_bill(bill: Bill, month: int) -> date:
    if month == bill.end.month:
        return bill.end
    return date(
        bill.end.year,
        month,
        get_days_in_month(bill.start.year, month),
    )


def get_days_in_month_for_bill(bill: Bill, month: int) -> int:
    month_start = get_month_start_for_bill(bill, month)
    month_end = get_month_end_for_bill(bill, month)
    td = month_end - month_start
    return td.days


def get_days_for_bill(bill: Bill) -> int:
    td = bill.end - bill.start
    return td.days


def get_amount_for_bill_in_month(bill: Bill, month: int) -> float:
    return (
        bill.amount * get_days_in_month_for_bill(bill, month) / get_days_for_bill(bill)
    )


def get_amount_for_bills_in_month(bills: List[Bill], month: int) -> float:
    return sum([get_amount_for_bill_in_month(bill, month) for bill in bills])


def main() -> None:
    bills: list[Bill] = [
        Bill(start=date(2024, 9, 12), end=date(2024, 10, 10), amount=149.83),
        Bill(start=date(2024, 10, 11), end=date(2024, 11, 8), amount=106.44),
        Bill(start=date(2024, 9, 10), end=date(2024, 10, 8), amount=152.44),
        Bill(start=date(2024, 10, 8), end=date(2024, 11, 8), amount=159.84),
        Bill(start=date(2024, 10, 1), end=date(2024, 10, 31), amount=40),
    ]
    amount = get_amount_for_bills_in_month(bills, 10)
    print(MESSAGE_FORMAT.format(amount, amount / NUM_RESIDENTS))


if __name__ == "__main__":
    main()
