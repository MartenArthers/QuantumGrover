# # bit string(s) to search for in the database
# SEARCH_TARGETS = [
#     "10101"[::-1],
#     "10100"[::-1],
# ]
#
# # number of shots to approximate the result of the program
# SHOT_COUNT = 10000
#
# # whether to apply optimisation to our generated QASM
# # performance improvement of ~20-50%
# OPTIMISE = True
#
# # MODES:
# #   - normal: use toffoli gates and ancillary bits for max speed
# #   - no toffoli: same as normal, but replace toffoli gates for 2-gate equivalent circuits. uses ancillary bits.
# #   - crot: no ancillary bits or toffoli gates, but scales with 3^n gates for n bits
# #   - fancy cnot: no ancillary bits or toffoli gates, scales 2^n
# MODE = "fancy cnot"
#
# # autogenerated parameters
# DATA_QUBITS = len(SEARCH_TARGETS[0])
#
# if MODE in ["crot", "fancy cnot"]:
#     ANCILLARY_QUBITS = 0
# elif MODE in ["normal", "no toffoli"]:
#     ANCILLARY_QUBITS = DATA_QUBITS - 3
# else:
#     raise ValueError("Invalid value for MODE: {}".format(MODE))
#
# QUBIT_COUNT = DATA_QUBITS + ANCILLARY_QUBITS
#
# SEARCH_TARGET_HEXES = list(map(lambda s: hex(int(s[::-1], 2))[2:],
#                                SEARCH_TARGETS))
