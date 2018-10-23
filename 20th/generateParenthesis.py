def generate(num):
    return generate_helper('', num, 0)


def generate_helper(curr, num_of_opening, num_of_closing):
    if num_of_opening == 0:
        return [curr + ')' * num_of_closing]
    elif num_of_closing == 0:
        return generate_helper(curr + '(', num_of_opening - 1, num_of_closing + 1)

    return generate_helper(curr + '(', num_of_opening - 1, num_of_closing + 1) + generate_helper(curr + ')', num_of_opening, num_of_closing - 1)

print(generate(0))


