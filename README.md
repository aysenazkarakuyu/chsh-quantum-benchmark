# CHSH Game Quantum Benchmark

A small Python benchmark comparing classical and quantum strategies in the **CHSH game**, a standard test of quantum entanglement.

## The CHSH game

Two players, Alice and Bob, cannot communicate during the game. A referee sends each of them a random bit, `x` to Alice and `y` to Bob. Each player answers with one bit, `a` and `b`. They win the round if:

```
a XOR b = x AND y
```

- **Best classical strategy:** at most **75%** win rate (the classical bound).
- **Quantum strategy:** if Alice and Bob share an entangled pair of qubits, they can reach **cos²(π/8) ≈ 85.4%** (Tsirelson's bound).

## How it works

| File | Description |
| --- | --- |
| `classical_agent.py` | Simulates the optimal deterministic classical strategy (both players always answer `0`), which wins 3 out of 4 input pairs. |
| `quantum_agent.py` | Builds the quantum strategy in Qiskit: a shared Bell pair, then measurement rotations chosen by each player's input (Alice: 0 or π/4, Bob: ±π/8). Runs each of the 4 input pairs on the Qiskit Aer simulator. |
| `benchmark.py` | Runs both strategies and plots their win rates against the classical bound and Tsirelson's bound. |

## Results

| Strategy | Win rate |
| --- | --- |
| Classical | ~75.0% |
| Quantum (simulated) | ~85.3% |
| Tsirelson's bound (theory) | 85.35% |

The quantum strategy clearly beats the classical limit and matches the theoretical maximum.

## Getting started

```bash
pip install qiskit qiskit-aer numpy matplotlib

python classical_agent.py   # classical win rate
python quantum_agent.py     # quantum win rate
python benchmark.py         # comparison chart
```

## Tech stack

Python · Qiskit · Qiskit Aer · NumPy · Matplotlib
