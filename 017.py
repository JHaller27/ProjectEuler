from utils.decorators import *


@memoize()
def count_letters(word: str):
    return len(word)


ONES_WORDS = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS_WORDS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS_WORDS = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def list_nums():
    for hundreds in ONES_WORDS:
        if hundreds is not None:
            prefix = f'{hundreds} hundred and '
            yield f'{hundreds} hundred'
        else:
            prefix = ''

        # Ones
        for w in filter(lambda w: w is not None, ONES_WORDS):
            yield f'{prefix}{w}'

        # Teens
        for w in TEENS_WORDS:
            yield f'{prefix}{w}'

        # Tens
        for tens in filter(lambda w: w is not None, TENS_WORDS):
            yield f'{prefix}{tens}'
            for ones in filter(lambda w: w is not None, ONES_WORDS):
                yield f'{prefix}{tens} {ones}'

    yield 'one thousand'

if __name__ == '__main__':
    count = 0
    for w in list_nums():
        count += sum(map(count_letters, w.split(' ')))
    print(count)

