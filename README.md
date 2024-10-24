# Turing Machine Simulator

A Python implementation of a Turing Machine simulator that demonstrates basic operations like binary increment, palindrome checking, and string copying.

## Table of Contents
- Overview
- Installation
- Project Structure
- Usage
- Examples
- Contributing

## Overview

This project implements a Turing Machine simulator with the following features:

- Basic tape operations (read, write, move left/right)
- Utility functions for common operations
- Three example simulations:
  1. Binary Increment

## Installation

1. Clone the repository:
   git clone https://github.com/akorojo/Turing-Machine-Simulator.git
   cd Turing-Machine-Simulator

2. Install the package in development mode:
   pip install -e .

## Project Structure

Turing-Machine-Simulator/
├── setup.py
├── main.py
├── README.txt
├── requirements.txt
├── turing_machine/
    ├── __init__.py
    ├── TuringMachineTape.py
    ├── TuringMachineUtility.py

## Usage

Run the main script to see all simulations:
   python main.py

### TuringMachineTape Class

The `TuringMachineTape` class provides the basic Turing Machine operations:

Example:
   from io import StringIO
   from turing_machine import TuringMachineTape

   # Create a tape with input
   tape = TuringMachineTape(StringIO("hello"))

   # Basic operations
   tape.read()      # Read current symbol
   tape.write(65)   # Write symbol at current position
   tape.left()      # Move head left
   tape.right()     # Move head right
   tape.debug()     # Display tape contents

### TuringMachineUtility Class

The `TuringMachineUtility` class provides helper functions:

Example:
   from turing_machine import TuringMachineUtility

   # Utility operations
   TuringMachineUtility.find_left(tape, symbol)     # Find symbol to the left
   TuringMachineUtility.find_right(tape, symbol)    # Find symbol to the right
   TuringMachineUtility.rewind(tape)                # Return to beginning
   TuringMachineUtility.insert_begin(tape)          # Insert BEGIN_SYMBOL

## Examples

### 1. Binary Increment
Increments a binary number by 1:

Input: "1101"
Output: "1110"
Command: simulate_binary_increment()

Example output:
=== Binary Increment Simulation ===

Initial tape:

| 1 | 1 | 0 | 1 |

| ^ | _ | _ | _ |

Final tape (after increment):

| 1 | 1 | 1 | 0 |

| _ | _ | ^ | _ |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Contact

Your Name - youremail@example.com
Project Link: https://github.com/akorojo/Turing-Machine-Simulator

## Acknowledgments

* Inspiration from classic Turing Machine implementations
* Python's StringIO for input stream handling
* All contributors and testers of this project