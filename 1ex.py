class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class FileOpen:
    def __init__(self, filename):
        self.file = None
        self.flag = False
        self.filename = filename

    def __enter__(self):
        self.file = open("my_program.txt", "w")
        self.opened = True
        return self.file

    def __exit__(self):
        if self.opened:
            self.file.close()
        self.opened = False


if __name__ == "__main":
    with FileOpen("my_program.txt") as f:
        f.write("Hello Sasha\n")
