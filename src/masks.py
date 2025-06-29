def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и возвращает ее маску в формате XXXX XX** **** XXXX
    """
    mask_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер аккаунта и возвращает его маску в формате ****************XXXX
    """
    mask_account_number = f"****************{account_number[-4:]}"
    return mask_account_number
