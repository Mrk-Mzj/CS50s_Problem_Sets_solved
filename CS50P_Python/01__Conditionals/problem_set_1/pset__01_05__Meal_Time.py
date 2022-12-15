def main():
    time = input("\nWhat time is it? (XX:XX)\n")
    time = time.strip()

    if ":" in time:
        # jeśli godzina jest zapisana prawidłowo

        hours = convert(time)

        if hours >= 7 and hours <= 8:
            print("breakfast")
        if hours >= 12 and hours <= 13:
            print("lunch")
        if hours >= 18 and hours <= 19:
            print("dinner")


def convert(time):

    chunks = time.split(":")
    hours = float(chunks[0]) + (float(chunks[1]) / 60)
    return hours


if __name__ == "__main__":
    main()
