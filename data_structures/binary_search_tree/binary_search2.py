#Search

def search(target, array):
    array = sorted(array)
    test_number = round(array / 2) 

    if test_number == target:
        return target 
    else:
        upper = [:test_number]
        lower = [test_number:]
        if target > test_number:
            test_number = round(array / 2)
            if test_number == target:
                return target
            else:

        test_number = round(array/2)
