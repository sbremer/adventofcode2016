
# This is that the assembunny code actually does, broken down and optimized
def func(a, b=0, c=0, d=0):
    output = []

    d = a + 2532
    #while True:  # Repeating infinitely
    a = d
    while a != 0:
        b = a
        a = int(b / 2)
        output.append(b % 2)

    return output


def main():
    a_init = 2730 - 2532
    output = func(a_init)
    output_str = ''.join([str(x) for x in reversed(output)])

    print('First alternating output ({}) occurs when initializing register a with: {}'.format(output_str, a_init))


if __name__ == '__main__':
    main()