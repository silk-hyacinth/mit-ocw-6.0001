# Problem Set 4A
# Name: Benjamin Wang
# Collaborators:
# Time Spent: 3 hours probably

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
    # inserts first character into each mem of list of all permutations of smaller sequence





    if len(sequence) == 1:
        return [sequence]
    else:
        new = []
        first_letter = sequence[:1]
        remaining_characters = sequence[1:]
        perms_of_remaining_chars = get_permutations(remaining_characters)
        # insert first letter into every iteration of remaining characters
        for permutation in perms_of_remaining_chars:
            for i in range(len(permutation)+1):
                #print(new)
                thing = permutation[:i]+first_letter+permutation[i:]
                new.append(thing)
        return list(set(new))
    # this is really, really, really difficult. I had to cheat this first time.
    # I think I will go and do some other recursion practice problems to familiarize myself with the technique.



if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #pass #delete this line and replace with your code here

    print(len(get_permutations("abcd")))

