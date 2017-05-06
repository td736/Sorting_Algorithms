from SelectionSort import SelectionSort
from InsertionSort import InsertionSort


def Main(array_to_be_sorted):
    
    acceptedTypes = [int, float, str] 
    
    assert (type(array_to_be_sorted) == list), "The input must be in the form of a list."
    
    for item in array_to_be_sorted:
        assert (type(item) in acceptedTypes) , "Type %s unaccepted." % str(type(item))

    assert array_to_be_sorted != [] , "The array must not be empty."
    
##      The code above is run before anything else
##      to insure the input is formatted correctly.
##      Can be edited if the accepted format/types change.
    
    sortChoice = input("\nWhich sorting algorith would you like to use?\n\n"+
                       "1. Selection Sort\n"+
                       "2. Insertion Sort\n\n"+
                       "Insert your choice: ")

    if sortChoice == "1":
        temp = SelectionSort(array_to_be_sorted)
        temp.sortFully()
        return temp.sorted
        del temp

    elif sortChoice == "2":
        temp = InsertionSort(array_to_be_sorted)
        temp.sortFully()
        return temp.sorted
        del temp
        
##      New sorting algorithms can be added
##      by simply adding a new option in sortChoice
##      and then adding a new elif statement here.
        
    else:
        raise ValueError("Invalid choice.")

      
##      Main loop. I've used return statements rather than print
##      above as it is a better design. As a results, the print
##      statements below are needed.    


if __name__ == '__main__':
    
    print("\nThe sorted array is;\n" +
          str(Main(eval(input("Insert array to be sorted: "))))
          + "\n")

    while input("Enter r to repeat, or press any other key to quit: ") == "r":
        
        print("\nThe sorted array is;\n" +
        str(Main(eval(input("\n\n\n\n\n\nInsert array to be sorted: "))))
        + "\n")



