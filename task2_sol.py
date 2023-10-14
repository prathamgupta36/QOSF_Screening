#*****************************
# Import necessary libraries
#*****************************
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from qiskit.visualization import plot_histogram

#************************************
# Function to find negative numbers
#************************************
def find_negative_numbers(list_number):
    # Determine the number of qubits required based on the list size
    n_qubits = len(list_number)
    
    # Create quantum registers for qubits and classical registers for measurement results
    qr = QuantumRegister(n_qubits, name="q")
    cr = ClassicalRegister(n_qubits, name="c")
    qc = QuantumCircuit(qr, cr)

    # Step 1: Apply Hadamard gates and conditional Z-gates for each qubit
    for i in range(n_qubits):
        # Step 2: Apply a Hadamard gate to prepare the qubit in superposition
        qc.h(qr[i])
        if list_number[i] < 0:
            # Step 3: If the number is negative, apply a Z gate to flip the qubit
            qc.z(qr[i])

     # Step 4: Apply Hadamard gates again
    for i in range(n_qubits):
        qc.h(qr[i])

    # Step 5: Measure the qubits
    for i in range(n_qubits):
        qc.measure(qr[i], cr[i])

    # Execute the quantum circuit using a quantum simulator
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts()

    # Step 6: Check if all measurement outcomes are '0', indicating no negative numbers
    for key in counts:
        if all(bit == '0' for bit in key):
            return False
            
    # If any measurement outcome is '1', at least one negative number was found
    return True

# Example usage
A = find_negative_numbers([1, 3, 2, -15])
print(A)  # Output: True

B = find_negative_numbers([1, 4, 8, 11])
print(B)  # Output: False

C = find_negative_numbers([-15, -14, 2, -1])
print(C)  # Output: True

D = find_negative_numbers([-5, 8, -3, 0, 10])
print(D)  # Output: True

E = find_negative_numbers([4, 7, 1, 12, 0])
print(E)  # Output: False

F = find_negative_numbers([0, -2, -4, -6, -8])
print(F)  # Output: True

G = find_negative_numbers([1, 2, 3, 4, 5])
print(G)  # Output: False

