from My_stack import Stack


# Task 2

def is_balanced(text):
    opening, closing = '([{', ')]}'
    stack = Stack()
    for character in text:
        if character in opening:
            stack.push(opening.index(character))
        elif character in closing:
            if stack and stack.peek() == closing.index(character):
                stack.pop()
            else:
                return f' Не сбалансированно'
    return f'Сбалансированно'


test_true_text = 'скобки ( п{р}авильно (вло[ж]ены))'
test_false_text = 'скобки НЕ [ пр(авильно вложены])'
print(f'{test_false_text} - {is_balanced(test_false_text)}')
print(f'{test_true_text} - {is_balanced(test_true_text)}')
