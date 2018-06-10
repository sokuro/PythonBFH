"""
    Function with SciFi Authors

    Extract last Name and use it as sorting Value
"""


scifi_authors = ["Isaac Asimov",
                 "Ray Bradbury",
                 "Robert Heinlein",
                 "Arthur C. Clarke",
                 "Frank Herbert",
                 "Orson Scott Card",
                 "Douglas Adams",
                 "H. G. Wells",
                 "Leigh Brackett"]


"""
    Build-in sort Function
    
    >> help(scifi_authors.sort)
"""


def main():

    # to access the last Name:
    # 1) split the String from Whitespace
    # 2) access by Index [-1]
    # 3) convert the String to lowercase, so that sort is NOT case-sensitive
    scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

    print(scifi_authors)


main()
