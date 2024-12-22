from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a Quantum Circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# Use AerSimulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

# Print compiled circuit
print(compiled_circuit)