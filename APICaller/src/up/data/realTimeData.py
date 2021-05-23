from typing import Iterable, Any

class tickerEntry():
    market = ""
    trade_date = ""
    trade_time = ""
    trade_date_kst = ""
    trade_time_kst = ""
    trade_timestamp = 0
    opening_price = 0.0
    high_price = 0.0
    low_price = 0.0
    trade_price = 0.0
    prev_closing_price = 0.0
    change = "FALL"
    change_price = 0.0
    change_rate = 0.0
    signed_change_price = 0.0
    signed_change_rate = 0.0
    trade_volume = 0.0
    acc_trade_price = 0.0
    acc_trade_price_24h = 0.0
    acc_trade_volume = 0.0
    acc_trade_volume_24h = 0.0
    highest_52_week_price = 0.0
    highest_52_week_date = ""
    lowest_52_week_price = 0.0
    lowest_52_week_date = ""
    timestamp = 0

    def __dir__(self) -> Iterable[str]:
        print(super.__dir__(self))
        attribute = [att for att in super.__dir__(self) if not att.startswith('_')]
        return attribute

    def __str__(self) -> str:
        result = ""
        attribute = [att for att in dir(self)]
        for a in attribute:
            result += str(a) + " : " + str(self.__getattribute__(a))

        return result

    def _getItems_(self):
        result = {}
        attribute = [att for att in dir(self)]
        for a in attribute:
            result.update({a:self.__getattribute__(a)})

        return result
    