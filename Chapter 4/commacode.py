def comma_code(list_value):
    result = ''
    if len(list_value) == 0:
        return ''
    elif len(list_value) == 1:
        return str(list_value)
    else:
        last_index = list_value[len(list_value) - 1]
        for n in list_value:
            if n == last_index:
                result += 'and ' + n
            else:
                result += n + ', '
        return result


if __name__ == '__main__':
    list_n = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(list_n))
