from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n_qubits = 2
qc = QuantumCircuit(n_qubits)

# Step 1: Superposition
qc.h(range(n_qubits))

# Step 2: Oracle for |10>
qc.x(0)
qc.mcx([0], 1)  # Multi-controlled X to flip phase of |10>
qc.x(0)

# Step 3: Measure
qc.measure_all()

# Simulate
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts()

print("Oracle Test:", counts)
