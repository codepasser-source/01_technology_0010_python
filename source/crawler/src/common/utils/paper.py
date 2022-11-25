#!/usr/bin/python3
# author: codepasser
# date: 2022/11/15

class Paper:
    total = None
    size = None

    def __init__(self, _total, _size):
        self.total = _total
        self.size = _size

    def total_page(self):
        _remainder = lambda x: (x + 1) if (self.total % self.size) > 0 else x
        _total_page = (self.total // self.size)
        return _remainder(_total_page)

    def pages(self, _start_zero=True):
        if _start_zero:
            return range(self.total_page())
        else:
            return range(1, self.total_page() + 1)
