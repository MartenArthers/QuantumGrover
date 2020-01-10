# bit string to search for in the database
SEARCH_TARGET = "1001010"[::-1]

# number of shots to approximate the result of the program
# it's recommended to use a small shot count for many data qubits
SHOT_COUNT = 16

# autogenerated parameters
DATA_QUBITS = len(SEARCH_TARGET)
CONTROL_QUBITS = DATA_QUBITS - 3
QUBIT_COUNT = DATA_QUBITS + CONTROL_QUBITS