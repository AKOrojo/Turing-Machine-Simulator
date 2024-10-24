from io import StringIO
from turing_machine import TuringMachineTape, TuringMachineUtility


def simulate_binary_increment():
    """
    Simulates a Turing machine that increments a binary number.
    Input format: A sequence of 0s and 1s
    Example: '1101' becomes '1110'
    """
    print("\n=== Binary Increment Simulation ===")
    # Create tape with initial binary number
    input_stream = StringIO("1101")
    tape = TuringMachineTape(input_stream)

    print("Initial tape:")
    tape.debug()

    # Move to the end of the number
    while tape.read() != TuringMachineTape.BLANK_SYMBOL:
        tape.right()
    tape.left()

    # Increment the binary number
    carry = 1
    while carry and tape.position >= 0:
        current = tape.read()
        if current == ord('0'):
            tape.write(ord('1'))
            carry = 0
        elif current == ord('1'):
            tape.write(ord('0'))
            carry = 1
        tape.left()

    if carry:
        # Need to add a new digit
        tape.right()
        TuringMachineUtility.shift_and_insert(tape, ord('1'))

    print("\nFinal tape (after increment):")
    tape.debug()


if __name__ == "__main__":
    try:
        # Run different simulations
        simulate_binary_increment()
        print("\nBinary increment completed successfully!")
    except SystemExit:
        pass

