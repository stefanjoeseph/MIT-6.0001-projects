# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]

    else:
        first_letter = sequence[0]
        rest_of_letters = sequence[1:]
        list_of_perms = get_permutations(rest_of_letters)

        copy_of_list = list_of_perms.copy()
        list_of_perms = []

        for element in copy_of_list:
            for i in range(len(element) + 1):
                new_element = element[:i] + first_letter + element[i:]
                list_of_perms.append(new_element)

        return list_of_perms








if __name__ == '__main__':
    # Test cases
    test_case_1 = 'abc'
    expected_output_1 = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    actual_output_1 = get_permutations(test_case_1)

    test_case_2 = 'her'
    expected_output_2 = ['her', 'ehr', 'erh', 'hre', 'rhe', 'reh']
    actual_output_2 = get_permutations(test_case_2)

    test_case_3 = 'ted'
    expected_output_3 = ['ted', 'etd', 'edt', 'tde', 'dte', 'det']
    actual_output_3 = get_permutations(test_case_3)

    print('---------------------------------')
    if expected_output_1 == actual_output_1:
        print('Test case 1:', test_case_1)
        print('Test case 1 passed')
    elif expected_output_1 != actual_output_1:
        print('Test case 1 failed')
    print('---------------------------------')

    if expected_output_2 == actual_output_2:
        print('Test case 2:', test_case_2)
        print('Test case 2 passed')
    elif expected_output_1 != actual_output_1:
        print('Test case 2 failed')
    print('---------------------------------')

    if expected_output_3 == actual_output_3:
        print('Test case 3:', test_case_3)
        print('Test case 3 passed')
    elif expected_output_3 != actual_output_3:
        print('Test case 3 failed')
    print('---------------------------------')


