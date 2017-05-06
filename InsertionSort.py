class InsertionSort():



    def __init__(self, data):
        self.unsorted = data
        self.sorted = []
        

    def sortFirstElement(self):
        """Moves the first element from the unsorted array to the sorted array."""
        self.sorted.append(self.unsorted[0])
        self.unsorted.remove(self.unsorted[0])

        
    def sortNextElement(self):
        """Picks the next element of the unsorteed list and adds
        it to its correct location in the sorted array """
        nextElement = self.unsorted[0]
        self.unsorted.remove(nextElement)

        if type(nextElement) == int or type(nextElement) == float:
            
            for item in self.sorted:
                
                if type(item) != str and item > nextElement:
                    self.sorted.insert(self.sorted.index(item),nextElement)
                    return True
                
                elif type(item) == str:
                    self.sorted.insert(self.sorted.index(item),nextElement)
                    return True
            """If the for loop doesn't find any item larger than the element
                being sorted, the element being sorted is placed at the end """
            self.sorted.append(nextElement) 


        elif type(nextElement) == str:
            """If there are no other strings in the sorted list, current string is
               placed at the end. Otherwise, it's placed in alphabetical order."""
            for item in self.sorted:
                if type(item) == str and sorted([item,nextElement])[0] == nextElement:
                    self.sorted.insert(self.sorted.index(item),nextElement)
                    return True
            
            self.sorted.append(nextElement) 

            
    def sortFully(self):
        """Calls the sort function until there are no elements in the unsorted list."""
        self.sortFirstElement()

        while self.unsorted != []:
            self.sortNextElement()
        
