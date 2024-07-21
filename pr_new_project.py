def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
# inner_function() - вызвать inner_function вне функции test_function не получится так как:
# inner_function не принадлежит глобальной области видимости.
