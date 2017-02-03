class TimeSeriesJSON:

    def __init__(self, f=None, fn=None):
        """
        :param f: file object (_io.TextIOWrapper)
        :param fn: file name as a string
        """
        if f is not None:
            self.__type = 'file'
            self.__file = f
        elif fn is not None:
            self.__type = 'file_name'
            self.__file_name = fn
            self.__file = open(fn)