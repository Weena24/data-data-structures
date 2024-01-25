# pylint: disable=missing-docstring

RATES = {'USDEUR': 0.85, 'GBPEUR': 1.13, 'CHFEUR': 0.86, 'EURGBP': 0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    print(amount, currency)
    print(amount[1], currency)
    print(f"{amount[1]}{currency}")
    print(amount[1] + currency)
    #print(RATES[f"{amount[1]}{currency}"])
    #print(amount[0]*RATES[f"{amount[1]}{currency}"])
    print(RATES.get(f"{amount[1]}{currency}"))
    if RATES.get(f"{amount[1]}{currency}"):
        return round(amount[0]*RATES[f"{amount[1]}{currency}"])
    return None
