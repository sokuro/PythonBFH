"""
* None is a build constraint that denotes the null
* Functions without the return statement return None by default
"""
def appent_to(element, to_list=None):
    if to_list is None:
        to_list = []
    to_list.append(element)
    return to_list
