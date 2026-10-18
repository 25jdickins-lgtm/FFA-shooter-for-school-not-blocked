import random
import time

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

def run_battle_royale():
    # Create a list of players
    names = ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah"]
    players = [Player(name) for name in names]

    print("=== WELCOME TO THE PYTHON BATTLE ROYALE ===")
    print(f"Starting with {len(players)} players: {[p.name for p in players]}\n")
    time.sleep(1)

    round_num = 1

    while len([p for p in players if p.is_alive]) > 1:
        print(f"--- Round {round_num} ---")
        
        # Filter living players
        alive_players = [p for p in players if p.is_alive]
        
        # Each living player attacks another random living player
        for attacker in alive_players:
            if not attacker.is_alive:
                continue
                
            targets = [p for p in alive_players if p != attacker and p.is_alive]
            if not targets:
                break
                
            defender = random.choice(targets)
            damage = random.randint(10, 35)
            defender.take_damage(damage)
            
            print(f"{attacker.name} hits {defender.name} for {damage} damage! ({defender.name} HP: {defender.health})")
            
            if not defender.is_alive:
                print(f"💀 {defender.name} has been eliminated!")
                
        print("")
        round_num += 1
        time.sleep(1.5)

    winner = [p for p in players if p.is_alive][0]
    print("=== BATTLE ENDED ===")
    print(f"👑 The winner is {winner.name} with {winner.health} HP remaining!")

if __name__ == "__main__":
    run_battle_royale()
