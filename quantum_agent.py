import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def build_chsh_circuit(x:int, y:int) -> QuantumCircuit:

    qc = QuantumCircuit(2,2)

    qc.h(0)
    qc.cx(0,1)
    qc.barrier()

    alpha=0.0 if x== 0 else np.pi/4
    qc.ry(-2 * alpha, 0)

    beta=np.pi/8 if y== 0 else -np.pi/8
    qc.ry(-2 * beta, 1)
    qc.barrier()

    qc.measure(0, 0)
    qc.measure(1, 1)

    return qc


def simulate_chsh_circuit(x: int, y: int, shots: int = 10_000) -> float:
    qc= build_chsh_circuit(x,y)
    simulator= AerSimulator()

    job=simulator.run(qc, shots=shots)
    counts=job.result().get_counts()

    round_wins=0
    for bitstring, count in counts.items():
        b=int(bitstring[0])
        a=int(bitstring[1])

        if (a ^ b) == (x & y):
            round_wins += count

    return round_wins / shots

def simulate_quantum_strategy(shots_pair: int = 5_000) -> float:

    total_wins = 0
    total_shots = 0

    for x in [0, 1]:
        for y in [0, 1]:
            round_win_rate = simulate_chsh_circuit(x, y, shots=shots_pair)
            total_wins += round_win_rate * shots_pair
            total_shots += shots_pair

    return total_wins / total_shots

if __name__ == "__main__":
    print("Quantum simulation is running...")
    win_rate = simulate_quantum_strategy(shots_pair=10_000)
    print(f"General Quantum Win Rate: %{win_rate * 100:.2f}")
    print(f"Theoretical Tsirelson Bound: %{((2 + np.sqrt(2)) / 4) * 100:.2f}")