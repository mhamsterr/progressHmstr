import math

class Bar(object):

    def __init__(self,
                 msg: str = " ",
                 symbol: str = "#",
                 empty_symbol: str = "-",
                 max_value: float = 100,
                 bar_format_symbol: str = " "):
        """
        Class of a bar
        ~~~
        Params:
        -- msg (str): Message that will display in front of progressbar
        -- symbol (str): A symbol that will display the progress
        -- empty_symbol (str): A symbol that will display job to do (or empty side of a bar)
        -- max_value (float or int): Maximum value of job to do
        -- bar_format_symbol (str): A symbol that will be placed right before and right after the progressbar (for Discord, forums etc)
        """
        self.__barSymbol = symbol
        self.__emptySymbol = empty_symbol
        self.__maxValue = max_value
        self.__currentValue = 0
        self.__barFormatSymbol = bar_format_symbol
        self.__percents = int(
            math.floor((int(self.__currentValue) / int(self.__maxValue)) * 25))
        self.__barLine = self.__barSymbol * self.__percents
        self.__emptyBarLine = self.__emptySymbol * (25 - self.__percents)
        self.__barString = f"{msg} {self.__barFormatSymbol}|{self.__barLine}{self.__emptyBarLine}| [{self.__currentValue}/{self.__maxValue}]{self.__barFormatSymbol} "

    def update(self, msg: str = " ", count: float = 1, action: str = " "):
        """
        Get bar string and update value
        ~~~
        Params:
        -- msg (str): A string that will be displayed in front of progressbar - Optional
        -- count (float or int): How much progress will be added to bar on update - Optional, defaults to 1
        -- action (str): A string that will be displayed after progressbar and "[Done/Max]" count - Optional
        """
        self.__currentValue = self.__currentValue + count
        if self.__currentValue >= self.__maxValue:
            self.__maxValue = self.__currentValue
        self.__percents = int(
            math.floor((int(self.__currentValue) / int(self.__maxValue)) * 25))
        self.__barLine = self.__barSymbol * self.__percents
        self.__emptyBarLine = self.__emptySymbol * (25 - self.__percents)
        self.__barString = f"{msg} {self.__barFormatSymbol}|{self.__barLine}{self.__emptyBarLine}| [{self.__currentValue}/{self.__maxValue}]{self.__barFormatSymbol}  {action}"
        return self.__barString

    def get(self, msg: str = " ", action: str = " "):
        """Get last bar string without updating"""
        self.__barString = f"{msg} {self.__barFormatSymbol}|{self.__barLine}{self.__emptyBarLine}| [{self.__currentValue}/{self.__maxValue}]{self.__barFormatSymbol} {action}"
        return self.__barString

