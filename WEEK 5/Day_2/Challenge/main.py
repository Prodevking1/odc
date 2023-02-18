class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = (len(items) + pageSize - 1) // pageSize
        self.currentPage = 1

    def getVisibleItems(self):
        startIndex = (self.currentPage - 1) * self.pageSize
        endIndex = startIndex + self.pageSize
        return self.items[startIndex:endIndex]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1

    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = self.totalPages

    def goToPage(self, pageNum):
        if pageNum >= 1 and pageNum <= self.totalPages:
            self.currentPage = pageNum


alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ['a', 'b', 'c', 'd']

p.nextPage()
print(p.getVisibleItems())  # ['e', 'f', 'g', 'h']

p.lastPage()
print(p.getVisibleItems())  # ['y', 'z']

p.goToPage(4)
print(p.getVisibleItems())  # ['w', 'x', 'y', 'z']            