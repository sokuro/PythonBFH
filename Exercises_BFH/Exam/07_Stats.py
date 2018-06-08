class Stats:
    """
        A Class for holistic Aggregates
    """

    def __init__(self, initial_values=None):
        """
            Initialize stats class with specified initial value
        """
        if initial_values is None:
            initial_values = []
        self.__values = initial_values
        self.__is_sorted = False

    def add(self, value):
        self.__is_sorted = True
        self.__values.insert(0, value)

    @property
    def median(self):
        self._assertSorted()
        return self.__values[int(len(self.__values) / 2)]

    @property
    def min(self):
        self._assertSorted()
        return self.__values[0]

    def _assertSorted(self):
        self.__values.sort()
        self.__is_sorted = True

    def __str__(self):
        return 'Stats: ' + ', '.join(str(x) for x in self.__values)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return sorted(self.__values) == sorted(other.__values)
        else:
            return False

    def __hash__(self):
        return hash((sorted(self.__values), self.__is_sorted))
