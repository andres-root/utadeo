#!/usr/bin/env python3


class Counter:
    def __init__(self, initial=0):
        self.count = initial

    def set_count(self, initial):
        self.counter = initial

    def get_count(self):
        return self.count

    def increment(self, delta=None):
        if delta:
            self.count += delta
        else:
            self.count += 1
        return self.get_count()

    def reset(self):
        self.count = 0
        return self.get_count()

    def __repr__(self):
        return 'Counter is: {}'.format(self.counter)
    
    def __str__(self):
        return 'Counter is: {}'.format(self.counter)



if __name__ == '__main__':
    counter = Counter()
    counter.increment()
    print(counter)
