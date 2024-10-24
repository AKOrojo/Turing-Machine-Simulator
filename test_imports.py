from io import StringIO
from turing_machine import TuringMachineTape, TuringMachineUtility


def test_imports():
    print("Testing imports...")

    # Test TuringMachineTape
    print("\nTesting TuringMachineTape:")
    tape = TuringMachineTape(StringIO("test"))
    print("Created tape successfully")

    # Test TuringMachineUtility methods
    print("\nTesting TuringMachineUtility methods:")
    print("Available methods:", [method for method in dir(TuringMachineUtility)
                                 if not method.startswith('_')])

    # Test specific method
    print("\nTesting insert_begin:")
    TuringMachineUtility.insert_begin(tape)
    print("insert_begin called successfully")


if __name__ == "__main__":
    test_imports()