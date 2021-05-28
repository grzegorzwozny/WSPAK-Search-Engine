import re

class wspak:
    def __init__(self, input):
        print ("*** WSPAK Search Engine ***")
        self.input = input

    def open_file(self):
        f = open(self.input, mode="r", encoding="utf8")
        return str(f.read())

    def clean(self):
        data = self.open_file()
        # mydict = {33:  None}
        data = re.sub("[!?()\{\},.''"";:’_*]", '', data)
        return data

    def chopping(self):
        data = []
        data = self.clean().split()
        return data

    def compare(self):
        out = []
        data = self.chopping()
        lenght = len(data)
        for idx, d in enumerate(data):
            d = d.lower()
            r = d[::-1]
            cnt = "{}/{}"
            print(cnt.format(idx, lenght))
            if len(d) > 3 and d == r:
                # str = "{} --> {}"
                # print(str.format(d, r))
                out.append(d)

        return print(out)