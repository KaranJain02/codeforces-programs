from bisect import bisect_left

class Set:
    def __init__(self, elems, alreadySorted):
        self._elements = elems.copy()
        if not alreadySorted:
            self._elements.sort()
    def cardinality(self):
        return len(self._elements)
    def add(self, e):
        i = bisect_left(self, e)
        found = i < len(self._elements) and self._elements[i] == e
        if not found:
            self._elements.insert(i, e)
    def remove(self, e):
        i = bisect_left(self._elements, e)
        found = i < len(self._elements) and self._elements[i] == e
        if found:
            self._elements.pop(i)
    def contains(self, e):
        i = bisect_left(self._elements, e)
        found = i < len(self._elements) and self._elements[i] == e
        return found
    def _merge(self, list1, list2, keepAll, keepDuplicate):
        i = 0
        j = 0
        list3 = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                if keepAll:
                    list3.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                if keepAll:
                    list3.append(list2[j])
                j += 1
            else:
                list3.append(list1[i])
                if keepDuplicate:
                    list3.append(list2[j])
                i += 1
                j += 1
        if keepAll:
            list3.extend(list1[i:])
            list3.extend(list2[j:])
        return list3
    def union(self, s):
        newElems = self._merge(self._elements, s._elements, True, False)
        return Set(newElems, True)
    def intersection(self, s):
        newElems = self._merge(self._elements, s._elements, False, False)
        return Set(newElems, True)

s1 = Set([3,2,1], False)
s2 = Set([3,4], False)
s3 = s1.union(s2)
s4 = s1.intersection(s2)
print(s3.contains(4))
print(s4.contains(4))
