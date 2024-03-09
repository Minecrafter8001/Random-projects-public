import keyboard
import random
import time

def simulate_key_press():
    keys = ['W', 'A', 'S', 'D']
    key_to_press = random.choice(keys)
    duration = random.uniform(1, 5)

    print(f"Pressing '{key_to_press}' for {duration:.2f} seconds...")
    
    keyboard.press(key_to_press)
    time.sleep(duration)
    keyboard.release(key_to_press)

if __name__ == "__main__":
    last_key = None

    try:
        while True:
            new_key = last_key
            while new_key == last_key:
                new_key = random.choice(['W', 'A', 'S', 'D'])

            simulate_key_press()
            last_key = new_key

            time.sleep(random.uniform(1, 5))
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
a