import pytest
from string_utils import StringUtils
Utils = StringUtils ()




# Тестирование функции конвертации перовй буквы текста в заглавную

@pytest.mark.parametrize ('inp, expected', 
[
    ('text', 'Text' ),
    ('123', '123'),
    ('мак', 'Мак'),
    ('Text','Text'),
    ('tEXT', 'TEXT'),
    ('TEXT', 'TEXT'),
    ('здравствуйте, Юрий Иванович', 'Здравствуйте, Юрий Иванович')
])
def test_capitalize_positive (inp, expected):
    assert Utils.capitilize (inp) == expected


@pytest.mark.xfail
@pytest.mark.parametrize ('inp, expected', 
[
    ('', '' ),
    (' ', ' '),
    (None, None),
    (123,123),
    ('test','test')
])
def test_capitalize_negative (inp, expected):
    assert Utils.capitilize (inp) == expected




#Тестирование функции автоматического удаления пробелов перед текстом

@pytest.mark.parametrize ('inp, expected', 
[
    (' test', 'test'),
    ('  123', '123'),
    ('Test test', 'Test test'),
    (' Test test', 'Test test'),
    ('    ', '')

])
def test_trim_positive (inp, expected):
    assert Utils.trim (inp) == expected


@pytest.mark.xfail
@pytest.mark.parametrize ('inp, expected', 
[
    (None,None),
    (123, '123'),
    (' Test', ' Test')
    
])
def test_trim_negative (inp, expected):
    assert Utils.trim (inp) == expected




#Тестирование функции по переработке текста в строки
@pytest.mark.testing
@pytest.mark.parametrize ('inp, expected',
[
    ('1,2,3', ['1', '2', '3']),
    ('Мы писали,мы писали,наши пальчики устали', ['Мы писали', 'мы писали', 'наши пальчики устали']),
    ('1', ['1']),
    ('T, ', ['T', ' '])
])
def test_to_list_positive (inp, expected):
    assert Utils.to_list (inp) == expected


@pytest.mark.xfail
@pytest.mark.parametrize ('inp, expected',
[
   (None, None),
   ('1,2,3', '1,2,3')
])
def test_to_list_negative (inp, expected):
    assert Utils.to_list (inp) == expected




#Тестирование функци по поиску символа в строке

@pytest.mark.parametrize ('text, symbol',
[
    ('Bad', 'B'),
    ('123456789', '4'),
    ('Мытищинский     дворник', ' '),
    ('Циклопентанпергидрофенантрен', 'пентан')
])
def test_contains_true_positive (text, symbol):
    assert Utils.contains (text, symbol) == True


@pytest.mark.parametrize ('text, symbol',
[
    ('Bad', 'N'),
    ('123456789', '0'),
    ('Мытищинский дворник', '-'),
])
def test_contains_false_positive (text, symbol):
    assert Utils.contains (text, symbol) == False


@pytest.mark.xfail
@pytest.mark.parametrize ('text, symbol',
[
  (123, '123'),
  ('123456789', 4),
  (None, None),
  ('Строка', None),
  ('Циклопентанпергидрофенантрен', '')
])
def test_contains_negative_false (text, symbol):
    assert Utils.contains (text, symbol) == False
   

@pytest.mark.xfail
@pytest.mark.parametrize ('text, symbol',
[
  (123, '123'),
  ('123456789', 4),
  (None, None),
  ('Строка', None),
  ('Циклопентанпергидрофенантрен', '') 
])
def test_contains_negative_True (text, symbol):
    assert Utils.contains (text, symbol) == True




#Тестирование функции удалдения подстроки из строки

@pytest.mark.parametrize ('text, symbol, after' ,
[
    ('Test', 't', 'Tes'),
    ('мама мыла раму, мама пьет вино', 'мама', ' мыла раму,  пьет вино'),
    ('Циклопентанпергидрофенантрен', 'пер', 'Циклопентангидрофенантрен'),
    ('1 2 3 4 5 6 7 8 9', ' ', '123456789'),
    ('A','A', ''),
    ('test', '', 'test'),
    ('test', 'a', 'test')
])
def test_delete_symbol_positive (text, symbol, after):
    assert Utils.delete_symbol (text, symbol) == after


@pytest.mark.xfail
@pytest.mark.parametrize ('text, symbol, after' ,
[
    ('Test', 't', 'Test'),
    (123, '1', 23),
    ('test','test', None)
])
def test_delete_symbol_negative (text, symbol, after):
    assert Utils.delete_symbol (text, symbol) == after



#Тестирование функции сравнения заданного и стартового символа

@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', 'T'),
    ('12345', '1'),
    ('сыр','с'),
    ('  Test', 'T')
])
def test_start_with_True_positive (Text, symbol):
    assert Utils.starts_with (Text, symbol) == True


@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', 'A'),
    ('12345', '2'),
    ('сыр','ы')
])
def test_start_with_False_positive (Text, symbol):
    assert Utils.starts_with (Text, symbol) == False


@pytest.mark.xfail
@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', ''),
    ('12345', 1),
    ('сыр',None)
])
def test_start_with_True_negative (Text, symbol):
    assert Utils.starts_with (Text, symbol) == True

@pytest.mark.xfail
@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', ''),
    ('12345', 1),
    ('сыр', None)
])
def test_start_with_False_negative (Text, symbol):
    assert Utils.starts_with (Text, symbol) == False




#Тестирование функции сравнения заданного и последнего символа

@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', 't'),
    ('12345', '5'),
    ('сыр','р'),
    ('Test   ', 't')
])
def test_end_with_True_positive (Text, symbol):
    assert Utils.end_with (Text, symbol) == True


@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', 'A'),
    ('12345', '2'),
    ('сыр','с')
])
def test_end_with_False_positive (Text, symbol):
    assert Utils.end_with (Text, symbol) == False


@pytest.mark.xfail
@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', ''),
    ('12345', 1),
    ('сыр', None)
])
def test_end_with_True_negative (Text, symbol):
    assert Utils.end_with (Text, symbol) == True


@pytest.mark.xfail
@pytest.mark.parametrize ('Text, symbol',
[
    ('Test', ''),
    ('12345', 1),
    ('сыр', None)
])
def test_end_with_False_negative (Text, symbol):
    assert Utils.end_with (Text, symbol) == False




#Тестирование функции обозначающей пустую строку

@pytest.mark.parametrize ('text',
[
    (''),
    ('     '),  
])
def test_is_empy_true(text):
    assert Utils.is_empty (text) == True


@pytest.mark.parametrize ('text',
[
    ('text'),
    ('     text'),
    ('   t e   x t   ')   
])
def test_is_empy_false(text):
    assert Utils.is_empty (text) == False


@pytest.mark.xfail
@pytest.mark.parametrize ('text',
[
    (None),
    (1),   
])
def test_is_empy_negative (text):
    assert Utils.is_empty (text) == True




#Преобразование списка в строку с указанным разделителем

@pytest.mark.parametrize ('inp, joiner, expected',
[
   (['1', '2', '3'], ',', '1,2,3'),
   ([1,2,3,4,5], ',', '1,2,3,4,5'),
   (['Мама', 'Папа', 'Я'], '4', 'Мама4Папа4Я')
])
def test_list_to_string_positive (inp, joiner, expected):
    assert Utils.list_to_string (inp, joiner) == expected

@pytest.mark.xfail
@pytest.mark.parametrize ('inp, joiner, expected',
[
   ("['1','2','3']", ',', '1,2,3'),
   (None, ',', None),
   
])
def test_list_to_string_negative (inp, joiner, expected):
    assert Utils.list_to_string (inp, joiner) == expected