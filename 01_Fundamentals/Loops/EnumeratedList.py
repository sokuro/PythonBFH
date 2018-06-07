class EnumeratedList:

    values = [1, 2, 3, 4, 5, 6]

    # inputValue = input("Enter a value: ")

    found_index = None

    for index, value in enumerate(values):
        if value == 5:
            found_index = index
            print('The value is in the Array')
            break
        print('The value is not in the array!')

    print('The value\'s index is: ', found_index)