import time

def loading_animation(duration=3, message="Loading"):
    animation = ["|", "/", "-", "\\"]
    # animation = ["", ".", "..", "..."]
    idx = 0
    start_time = time.time()

    while (time.time() - start_time) < duration:
        print(f"\r{message} {animation[idx % len(animation)]}", end="", flush=True)
        idx += 1
        time.sleep(0.1)

    print("\rEND          ")

# if __name__ == "__main__":
#     loading_animation()

# loading_animation(1, "Espera")
# Espera \/