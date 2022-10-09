'''
program on split and join methods in python (hackerrank)
'''


def split_and_join(txt):
    # write your code here
    txt = txt.split()
    txt = "-".join(txt)
    return txt

if __name__ == '__main__':
    txt = input()
    result = split_and_join(txt)
    print(result)