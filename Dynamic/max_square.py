# Input is the length of several consecutive beams, need to find a max square size formed by them #

planks = [11, 12, 11, 9, 13, 77, 9, 1, 79, 12, 11, 5, 28] # Example

def build_roof(planks):
    '''Takes the input, assigns every plank size its amount, then finds max_size, linear time'''
    planks.sort(reverse=True)
    sizes = list(set(planks))
    sizes.sort(reverse=True)
    amount = {}
    max_size = 0

    for i in sizes:
        amount[i] = planks.count(i)
        width = sum([amount[j] for j in sizes if j >= i])
        if i < width:
            if max_size < i:
                max_size = i
        else:
            if max_size < width:
                max_size = width
    return max_size

if __name__ == '__main__':
    print(build_roof(planks))
