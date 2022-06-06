def get_ratios(list1, list2):
    """
    Assumptions: list 1 nd 2 are lists of equal length
    Returns: a list containing list1[i] / list2[i]
    """
    ratios = []
    for index in range(len(list1)):
        try: 
            ratios.append(list2[index]/float(list2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('called function has bad arguments')
    return ratios

L1 = [1,2,3]
L2 = [4,5,6]
L3 = [7,8]

