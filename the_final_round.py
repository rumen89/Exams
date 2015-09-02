# 1. Count words

# Given a list of strings, implement a function, called count_words(arr) 
# which returns a dictionary of the following kind:

# { "word" : count }
# Where count is the count of occurrences of the word in the list arr.

# Signature

# def count_words(arr):
#     pass
# Test examples

# >>> count_words(["apple", "banana", "apple", "pie"])
# {'apple': 2, 'pie': 1, 'banana': 1}
# >>> count_words(["python", "python", "python", "ruby"])
# {'ruby': 1, 'python': 3}

def count_words(arr):
    result = {}

    # counter = 1

    for word in arr:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    return result




# 2. Unique words

# Implement a function, called unique_words_count(arr) 
# which returns the number of different words in arr.

# arr is a list of strings.

# Signature

# def unique_words_count(arr):
#     pass
# Test examples

# >>> unique_words_count(["apple", "banana", "apple", "pie"])
# 3
# >>> unique_words_count(["python", "python", "python", "ruby"])
# 2
# >>> unique_words_count(["HELLO!"] * 10)
# 1

def unique_words_count(arr):
    result = 0

    unique_words = []

    for word in arr:
        if word not in unique_words:
            unique_words += [word]
            result += 1

    return result



# 3. NaN Expand

# In most programming languages, NaN stands for Not a Number.

# If we take a look at the following JavaScript code:

# typeof NaN === 'number' // true
# We will see that in JavaScript, NaN stands for Not a NaN, which is recursive by nature.

# Implement a Python function, called nan_expand(times), 
# which returns the expansion of NaN (In JavaScript terms :P) that many times.

# For example:

# If we expand NaN once (times=1), we will have "Not a NaN"
# If we expand NaN twice (times=2), we will have "Not a Not a NaN"
# If times=3, we have "Not a Not a Not a NaN"
# And so on ...
# Examples

# >>> nan_expand(0)
# ""
# >>> nan_expand(1)
# "Not a NaN"
# >>> nan_expand(2)
# "Not a Not a NaN"
# >>> nan_expand(3)
# "Not a Not a Not a NaN"

def nan_expand(times):
    result = ""

    while True:
        result += "Not a "
        times -= 1

        if times == 0:
            break

    result += "NaN"

    return result



# 4. Iterations of NaN Expand

# Implement a function, called iterations_of_nan_expand(expanded) that takes a string expanded,
# which is an unkown iteration of NaN Expand (check the problem for more information)

# The function should return the number of iterations that have been made, 
# in order to get to expanded.

# For example, if we have "Not a Not a Not a NaN" - this is the 3rd iteration of NaN.

# If expanded is not a valid NaN expand string, the function should return false! 
# (This is the hard part)

# Examples

# >>> iterations_of_nan_expand("")
# 0
# >>> iterations_of_nan_expand("Not a NaN")
# 1
# >>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
# 10
# >>> iterations_of_nan_expand("Show these people!")
# False

def iterations_of_nan_expand(expanded):
    result = 0

    nan = ""

    n = 0
    m = 6

    while True:
        for i in range(n, m):
            nan += expanded[i]

        if nan == "Not a ":
            result += 1
            nan = ""

        if (m + 6) <= len(expanded):
            n += 6
            m += 6
        else:
            break

    if result == 0:
        return False

    return result





def main():
    # print(count_words(["python", "python", "python", "ruby"]))
    # print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(iterations_of_nan_expand(nan_expand(11)))
    print(iterations_of_nan_expand("hello my friend"))



if __name__ == '__main__':
    main()