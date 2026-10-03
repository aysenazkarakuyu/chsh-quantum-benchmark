import matplotlib.pyplot as plt
from classical_agent import simulate_classical
from quantum_agent import simulate_quantum_strategy


classical_result = simulate_classical(trials=10_000) * 100    # Yields ~75.0%
quantum_result = simulate_quantum_strategy(shots_pair=2_500) * 100  # Yields ~85.3%

labels = ['Classical', 'Quantum']
values = [classical_result, quantum_result]

plt.bar(labels, values, color=['royalblue', 'darkviolet'])

plt.axhline(75.0, color='gray', linestyle='--', label='Classical Bound (75%)')
plt.axhline(85.35, color='crimson', linestyle='--', label="Tsirelson's Bound (85.35%)")

plt.ylim(0, 100)
plt.ylabel('Win Rate (%)')
plt.title('CHSH Game Performance Benchmark')
plt.legend(loc='lower right')

plt.show()