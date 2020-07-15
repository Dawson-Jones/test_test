class Match(object):
    def __init__(self, s):
        self.s = s
        self.count = 0


class S(object):
    def __init__(self, s):
        self.s = s

    def having(self, *args) -> bool:
        """

        :param args:
        :return:
        """
        res = dict()
        for s in args:
            if not isinstance(s, str):
                raise ValueError("all params muse be string")
            res[s] = False

        for c in self.s:
            for s in args:
                s_match = Match(s)
                if c == s_match[s_match.count]:
                    s_match.count += 1





if __name__ == '__main__':
    s = S("i have a apple, i have a pen. uhh, apple pen")
    str_li = ["apple", "pen", "applee"]
    s.having(str_li)