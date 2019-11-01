def generator_1(titles):
    for title in titles:
        yield title


def generator_2(titles):
    yield from titles


titles = ['Python', 'Java', 'C++']
for title in generator_1(titles):
    print('生成器1:', title)
for title in generator_2(titles):
    print('生成器2:', title)
