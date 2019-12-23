from argparse import ArgumentParser

def valid_word(word, valid_letters):
    contains_center = False
    for letter in word:
        if letter not in valid_letters:
            return False
        if letter is center_letter:
            contains_center = True

    return contains_center


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-c', '--center-letter',
        type=str,
        help='Center letter that must be included'
        )
    parser.add_argument(
        '-ol',
        '--outside-letters',
        nargs='+',
        help=('Outside letters that may/may not be used.'
              'List with a space between each')
    )
    args = parser.parse_args()

    center_letter = args.center_letter
    other_letters = args.outside_letters
    valid_letters = other_letters + [center_letter]

    if len(other_letters) != 6:
        raise Exception('Not exactly 6 outside letters.')
    for letter in valid_letters:
        if len(letter) > 1:
            raise Exception('Letters only.')

    txt = open('wordsEn.txt').readlines()
    answers = []
    for word in txt:
        word = word[:-1] # Strip new line char
        if len(word) >= 4 and valid_word(word, valid_letters):
            answers.append(word)

    answers.sort(key = len, reverse=True)
    print('Possible Answers')
    print('-'*16)
    for i, word in enumerate(answers):
        print(str(i+1)+'.', word)
