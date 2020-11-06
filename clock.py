from datetime import datetime


class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return "%s:%s:%s" % (self.__hour, self.__minute, self.__second)

    def __repr__(self):
        return "%s:%s:%s" % (self.__hour, self.__minute, self.__second)

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute

    def second(self):
        return self.__second

    def set_hour(self, new_hour):
        if 0 <= new_hour <= 23:
            self.__hour = new_hour
        else:
            raise ValueError("new_hour passed to set_hour was not in range [0, 23]")

    def set_minute(self, new_minute):
        if 0 <= new_minute <= 59:
            self.__minute = new_minute
        else:
            raise ValueError("new_minute passed to set_minute was not in range [0, 59]")

    def set_second(self, new_second):
        if 0 <= new_second <= 59:
            self.__second = new_second
        else:
            raise ValueError("new_second passed to set_second was not in range [0, 59]")

    def advance_hour(self, amount_to_advance):
        if amount_to_advance < 0:
            raise ValueError("amount_to_advance passed to advance_hour is negative")

        self.__hour = (self.__hour + amount_to_advance) % 24

    def advance_minute(self, amount_to_advance):
        if amount_to_advance < 0:
            raise ValueError("amount_to_advance passed to advance_minute is negative")

        self.__minute = self.__minute + amount_to_advance
        while self.__minute >= 60:
            self.advance_hour(1)
            self.__minute = self.__minute - 60

    def set_to_current_time(self):
        now = datetime.now()
        self.__hour = now.hour
        self.__minute = now.minute
        self.__second = now.second

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.__hour == other.hour() and self.__minute == other.minute() and self.__second == other.second()
        return False

    def __lt__(self, other):
        if isinstance(other, Clock):
            if self.__hour < other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute < other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second < other.__second:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Clock: " % other)

    def __gt__(self, other):
        if isinstance(other, Clock):
            if self.__hour > other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute > other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second > other.__second:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Clock: " % other)
