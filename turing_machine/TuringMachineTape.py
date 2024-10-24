class TuringMachineTape:
    BLANK_SYMBOL = -1
    BEGIN_SYMBOL = 1
    UTILITY_SYMBOL = -9999

    def __init__(self, input_stream=None):
        """
        Construct a tape with input read from the given stream (or no input at all)
        """
        self.tape = []
        self.position = 0

        if input_stream is not None:
            line = input_stream.readline()
            self.tape.extend(ord(c) for c in line)

        if len(self.tape) == 0:
            self.tape.append(self.BLANK_SYMBOL)

    def read(self):
        """Return the symbol at the head"""
        return self.tape[self.position]

    def write(self, symbol):
        """Write given symbol at the head"""
        if symbol == self.BLANK_SYMBOL:
            self.reject()
        self.tape[self.position] = symbol

    def right(self):
        """Move right"""
        self.position += 1
        if len(self.tape) <= self.position:
            self.tape.append(self.BLANK_SYMBOL)

    def left(self):
        """Move left"""
        if self.position <= 0:
            self.reject()
        self.position -= 1

    def debug(self, out=None):
        """Dump the contents of the tape"""
        import sys
        out = out or sys.stdout

        # Calculate widths for formatting
        widths = []
        for i in self.tape:
            term = f"<{i}>" if i < 32 else str(chr(i))  # Handle control characters
            widths.append(len(term))
            out.write(f"| {term} ")
        out.write("|\n")

        # Print position marker
        for i in range(len(self.tape)):
            c = "^" if i == self.position else " "
            out.write(f"| {c:{widths[i]}} ")
        out.write("|\n")
        out.flush()

    @staticmethod
    def accept():
        """Accept and exit"""
        print("accept")
        import sys
        sys.exit(0)

    @staticmethod
    def reject():
        """Reject and exit"""
        print("reject")
        import sys
        sys.exit(0)