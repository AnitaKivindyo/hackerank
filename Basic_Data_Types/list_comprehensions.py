'''
[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]

This is equivalent to writing:

results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )


For example, if you want to generate all combinations of lists [1,2,3] and [4,5,6] , write:

        >>> print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
            [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

It is equivalent to 

        >>> results = []
        >>> for x in [1, 2, 3]:
        ...     for y in [4, 5, 6]:
        ...         results.append([x, y])
        ... 
        >>> print(results)
        [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
'''


if __name__=='__main__':

    x= int(input('enter x:'))
    y= int(input('enter y:'))
    z= int(input('enter z:'))
    n= int(input('enter n:'))

    perms = [[i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n]

    print(perms)

 