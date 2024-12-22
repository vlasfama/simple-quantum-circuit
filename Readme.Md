# Simple Quantum Circuit Simulator

This project demonstrates a simple quantum circuit simulation using Qiskit and Qiskit Aer. The quantum circuit includes a single qubit, applies a Hadamard gate to create superposition, and measures the result.

## Prerequisites

- Python 3.10 or higher
- Qiskit and Qiskit Aer installed

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vlasfama/simple-quantum-circuit.git
   cd simple-quantum-circuit
   ```

2. Requirements:

    ```bash
    qiskit==0.45.0
    qiskit-aer==0.16.0
    ```

3. Run:

     ```bash
      python circuit.py
    ```

  Output:

          ┌───┐ ░ ┌─┐
     q: ┤ H ├─░─┤M├
        └───┘ ░ └╥┘
meas: 1/═════════╩═
                 0
  