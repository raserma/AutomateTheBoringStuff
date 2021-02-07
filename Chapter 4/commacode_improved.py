#! python3

def comma_code(my_list):
    for i in range(len(my_list) - 1):
        print(my_list[i], end=', ')
    print('and ' + my_list[i+1])


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cat']
    comma_code(spam)
