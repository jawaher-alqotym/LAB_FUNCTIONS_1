def print_trangle(num: int = 5) -> str:
    '''
    this function  takes 1 parameter of type int , then it prints out as a trangle.
    '''
    str_num = ''
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            str_num += ' '+str(j)
        print(str_num)
        str_num = ''

print_trangle()
print(print_trangle.__doc__)
