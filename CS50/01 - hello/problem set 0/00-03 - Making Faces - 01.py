# https://cs50.harvard.edu/python/2022/psets/0/


def main():
    face = input("Say something: ")
    print(convert(face))


def convert(face):

    face = face.replace(":)", "🙂")
    face = face.replace(":-)", "🙂")

    face = face.replace(":(", "🙁")
    face = face.replace(":-(", "🙁")

    return face


if __name__ == "__main__":
    main()
