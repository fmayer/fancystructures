""" Disjoint sets represented as rooted tree. """

class Set(object):
    __slots__ = ['rank', 'p']
    def __init__(self):
        self.rank = 0
        self.p = self

    def _link(self, other):
        if self is other:
            return
        if self.rank > other.rank:
            other.p = self
        else:
            self.p = other
            if self.rank == other.rank:
                other.rank += 1

    def union(self, other):
        """ Indicate two sets are equal. """
        self.find_set()._link(other.find_set())

    def _find_set(self):
        this = self
        while this is not this.p:
            this = this.p
        return this

    def _set_set(self, x):
        this = self
        while this is not this.p:
            p = this.p
            this.p = x
            this = p
        return x

    def find_set(self):
        """ Get canonical object for this set. """
        return self._set_set(self._find_set())
