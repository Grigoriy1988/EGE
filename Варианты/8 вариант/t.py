class LeftParagraph:
    def __init__(self,field_width):
        self.width = field_width
        self.words = []
        self.line = []
        self.string_length = 0
    def add_word(self,word):
        if self.string_length == 0:
            space = 0
        else:
            space = 1
        if self.string_length + space + len(word) <= self.width:
            self.words.append(word)
            self.string_length += len(word) + space
        else:
            self.line.append(' '.join(self.words))
            self.words = [word]
            self.string_length = len(word)
    def end(self):
        print(*self.line,sep='\n')
        print(' '.join(self.words))
        self.words = []
        self.line = []
        self.string_length = 0

class RightParagraph():
    def __init__(self, field_width):
        self.width = field_width
        self.words = []
        self.line = []
        self.string_length = 0

    def add_word(self,word):
        if self.string_length == 0:
            space = 0
        else:
            space = 1
        if self.string_length + space + len(word) <= self.width:
            self.words.append(word)
            self.string_length += len(word) + space
        else:
            line = ' '.join(self.words)
            line = ' ' * (self.width - len(line)) + line
            self.line.append(line)
            self.words = [word]
            self.string_length = len(word)
    def end(self):
        print(*self.line,sep='\n')
        line = ' '.join(self.words)
        line = ' ' * (self.width - len(line)) + line
        print(line)
        self.words = []
        self.line = []
        self.string_length = 0

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()