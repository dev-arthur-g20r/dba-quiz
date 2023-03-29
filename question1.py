numbers = [5, 1, 4, 6, 7, 3, 5, 7, 3]
filterIterator = filter(lambda number: (numbers.count(number) > 1), numbers)
uncleanList = list(filterIterator)
filteredNumbersSet = set(uncleanList)
filteredNumbersList = list(filteredNumbersSet)
print(filteredNumbersList)