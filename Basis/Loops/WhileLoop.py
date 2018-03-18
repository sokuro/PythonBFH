class WhileLoop:

    count = 0

    while count < 10:

        if count == 5:
            print('The value 5 is reached! Breaking!')
            break

        print('The count is: ', count)
        count = count + 1
