from .TuringMachineTape import TuringMachineTape

class TuringMachineUtility:
    @staticmethod
    def find_left(t: TuringMachineTape, symbol):
        """Seek to the left until we find the given symbol"""
        while t.read() != symbol:
            t.left()

    @staticmethod
    def find_right(t: TuringMachineTape, symbol):
        """Seek to the right until we find the given symbol"""
        while t.read() != symbol and t.read() != TuringMachineTape.BLANK_SYMBOL:
            t.right()
        if t.read() != symbol:
            t.reject()

    @staticmethod
    def rewind(t: TuringMachineTape):
        """Go left back to BEGIN_SYMBOL, then advance one"""
        TuringMachineUtility.find_left(t, TuringMachineTape.BEGIN_SYMBOL)
        t.right()

    @staticmethod
    def shift_and_insert(t: TuringMachineTape, symbol):
        """
        Open a space at the current head position by shifting everything to
        the right by one, then write the given symbol at that position
        """
        saved = t.read()
        t.write(TuringMachineTape.UTILITY_SYMBOL)
        while saved != TuringMachineTape.BLANK_SYMBOL:
            t.right()
            saved_next = t.read()
            t.write(saved)
            saved = saved_next

        TuringMachineUtility.find_left(t, TuringMachineTape.UTILITY_SYMBOL)
        t.write(symbol)
        t.right()

    @staticmethod
    def insert_begin(t: TuringMachineTape):
        """Insert the special BEGIN_SYMBOL at the current position of the head"""
        TuringMachineUtility.shift_and_insert(t, TuringMachineTape.BEGIN_SYMBOL)