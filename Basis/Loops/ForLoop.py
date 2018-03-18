class ForLoop:

    edibles = ["apple", "peach", "pineapple", "plum"]

    for fruit in edibles:
        if fruit == "peach":
            print("Peach is nowadays not fresh!")
            continue

        print("This fruit is fresh and delicious.")

    else:
        print("The is other time to consume this!")