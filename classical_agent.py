import random

def simulate_classical(trials: int =10_000) -> float:
    wins = 0

    a=0
    b=0

    for i in range(trials):
        x= random.choice([0,1])
        y= random.choice([0,1])
        
        if (a ^ b) == (x & y):
            wins +=1

    win_rate=wins/trials

    return win_rate

if __name__ == "__main__":
    trials = 20_000
    rate = simulate_classical(trials)
    print(f"Classical win rate ({trials} trials): %{rate * 100:.2f}")


    


