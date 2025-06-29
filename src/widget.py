from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    1. Принимает номер счета и возвращает его маску в формате ****************XXXX
    2. Принимает номер карты и возвращает ее маску в формате XXXX XX** **** XXXX
    """
    out_account_card = "".join(letter if letter.isdigit() else "" for letter in account_card)
    if len(out_account_card) == 16:
        return get_mask_card_number(out_account_card)
    elif len(out_account_card) == 20:
        return get_mask_account(out_account_card)
    else:
        return "Ошибка чтения параметров"


def get_date(format_date: str) -> str:
    """
        1. Принимает неотформатированную строку даты, и возвращает ее в формате ДД.ММ.ГГГГ
        """
    return f"{format_date[8:10]}.{format_date[5:7]}.{format_date[:4]}"