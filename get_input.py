import requests
import os


def get_input_from_web(day):
    url = 'http://adventofcode.com/2016/day/{}/input'.format(day)

    # session.txt contains the session token, taken from browser
    with open('data/session.txt', 'r') as file:
        cookie = {'session': file.read()}

    request = requests.get(url, cookies=cookie)

    with open('data/input_{}.txt'.format(day), 'w') as file:
        file.write(request.text)
        file.flush()

    return request.text


def get_input(day):
    if not os.path.exists('data/input_{}.txt'.format(day)):
        get_input_from_web(day)

    with open('data/input_{}.txt'.format(day), 'r') as file:
        return file.read()


# Testing
if __name__ == '__main__':
    get_input_from_web(1)
