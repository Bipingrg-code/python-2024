import os

if __name__ == "__main__":
    print("-----------------------")
    print("Welcome to RoboSpeaker 1.1.")
    print("----------------------")

    while True:
        x = input("Enter what you want me to speak. (Enter 'q' to quit): ")
        if x.lower() == "q":
            os.system("espeak 'Jaa Jaa Kaam gar'")
            break
        command = f"espeak '{x}'"

        os.system(command)
