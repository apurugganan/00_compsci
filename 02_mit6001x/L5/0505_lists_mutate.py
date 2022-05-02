## ALIASING
hot = ['yellow','orange', 'red']
warm = hot
hot.append('pink') # will also change warm (points to the same object)
print(warm) # same as hot


## CLONING
cool = ['blue', 'green', 'grey']
chill = cool[:]
cool.append('teal')
print(chill) # will differ from cool

## MUTATION 
# unexpected outcome
def remove_duplicate_wrong(l1,l2):
    for el in l1:
        if el in l2:
            l1.remove(el)

# correct way
def remove_duplicate_correct(l1,l2):
    l1_copy = l1[:]
    for el in l1_copy:
        if el in l2:
            l1.remove(el)
