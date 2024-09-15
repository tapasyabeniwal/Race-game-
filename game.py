import time
import random

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0

    def accelerate(self):
        self.speed += random.randint(1, 10)

    def brake(self):
        self.speed -= random.randint(1, 5)
        if self.speed < 0:
            self.speed = 0

    def update_distance(self):
        self.distance += self.speed

def game():
    player1 = Car("Player 1")
    player2 = Car("Player 2")

    print("Welcome to the racing game!")
    print("The game will last for 10 seconds.")

    start_time = time.time()
    while time.time() - start_time < 10:
        print(f"\n{player1.name}'s speed: {player1.speed} | {player2.name}'s speed: {player2.speed}")
        print(f"{player1.name}'s distance: {player1.distance} | {player2.name}'s distance: {player2.distance}")

        action1 = input(f"What would you like to do, {player1.name}? (accelerate/brake): ")
        action2 = input(f"What would you like to do, {player2.name}? (accelerate/brake): ")

        if action1.lower() == "accelerate":
            player1.accelerate()
        elif action1.lower() == "brake":
            player1.brake()

        if action2.lower() == "accelerate":
            player2.accelerate()
        elif action2.lower() == "brake":
            player2.brake()

        player1.update_distance()
        player2.update_distance()

        time.sleep(1)

    print("\nGame over!")
    print(f"{player1.name}'s final distance: {player1.distance} | {player2.name}'s final distance: {player2.distance}")

    if player1.distance > player2.distance:
        print(f"{player1.name} wins!")
    elif player2.distance > player1.distance:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    game()
