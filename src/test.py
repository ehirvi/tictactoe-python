class Foo:
    def __init__(self) -> None:
        self.bar()

    def bar(self):
        while int(input("Input (0-1): ")) != 1:
            print("Täällä ollaan")
        return

def main():
    foo = Foo()
    print("Meni läpi")

main()