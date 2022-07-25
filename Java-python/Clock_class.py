class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self._hour = hour
        self._minute = minute
        self._second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if hour > 23:
            self._hour = 0
        else:
            self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if minute > 59:
            minute = 0
        else:
            self._minute = minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second > 59:
            second = 0
        else:
            self._second = second

    def displayTime(self):
        return self._hour, ":", self._minute, ":", self._second
