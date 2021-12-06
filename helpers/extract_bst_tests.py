import re


def main():
    with open('../bst/tests/test_bst.py', 'r') as file:
        content = file.read()

    funcs = re.findall(r'def [\s\S]*?\(', content)
    for func in funcs:
        # print(func)
        test_name = func[len('def '):-1]
        with_exception = test_name.endswith('with_exception')
        if with_exception:
            method_name = test_name[len('test_bst_'):-len('_with_exception')]
            message = f'тест, проверяющий, что произошло ожидаемое исключение при выполнении метода \\verb|{method_name}|.'
        else:
            method_name = test_name[len('test_bst_'):]
            message = f'тест, проверяющий корректное поведение при выполнении метода \\verb|{method_name}|.'
        print(f'\\verb|{test_name}| --- {message}\n')


if __name__ == '__main__':
    main()