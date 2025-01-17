class LineSeekableFile:
    """
    https://stackoverflow.com/a/59185917/15980119
    """

    def __init__(self, seekable):
        self.fin = seekable
        self.line_map = list()  # Map from line index -> file position.
        self.line_map.append(0)
        while seekable.readline():
            self.line_map.append(seekable.tell())

    def __getitem__(self, index):
        # NOTE: This assumes that you're not reading the file sequentially.
        # For that, just use 'for line in file'.
        self.fin.seek(self.line_map[index])
        return self.fin.readline()


if __name__ == '__main__':
    with open("./line_seekable_file.py", "r") as file:
        file = LineSeekableFile(file)

        print(file[0])
        print(file[3])
