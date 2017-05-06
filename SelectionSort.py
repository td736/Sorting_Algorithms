class SelectionSort():



    def __init__(self, data):
        self.unsorted = data
        self.sorted = []


    def sortNextElement(self):
        """Finds the smallest element in the list."""
        minimum = self.unsorted[0]
        
        
        for item in self.unsorted:
        
            if type(item) == int or type(item) == float:
                
                if type(minimum) == str:
                    minimum = item
                    
                elif item < minimum:
                    minimum = item

                        
            elif type(item) == str and type(minimum) == str:
                minimum = sorted([item,minimum])[0]
                
        """Once the smallest element is found, it is added to the
           sorted portion and removed from the unsorted portion."""
        self.sorted.append(minimum)
        self.unsorted.remove(minimum)


    def sortFully(self):
        """Calls the sort function until the unsorted list is empty."""
        while self.unsorted != []:
            self.sortNextElement()
