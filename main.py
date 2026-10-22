import sys


def main():
    args = sys.argv[1:]
    if not args:
        print('usage: main.py <input>')
        return 1
    print(f'got: {args}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
