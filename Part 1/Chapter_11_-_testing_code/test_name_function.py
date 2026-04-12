from name_function import get_formatted_name

def test_first_last_name():
    """Поддерживаются ли имена типа "Настя Шкурина"?"""
    formatted_name = get_formatted_name('настя', 'шкурина')
    assert formatted_name == 'Настя Шкурина'