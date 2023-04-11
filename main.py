import typing


class decomposer:
    first_sound_list = [
        'ㄱ', ['shift', 'ㄱ'], 'ㄴ', 'ㄷ', ['shift', 'ㄷ'], 'ㄹ',
        'ㅁ', 'ㅂ', ['shift', 'ㅂ'], 'ㅅ', ['shift', 'ㅅ'], 'ㅇ',
        'ㅈ', ['shift', 'ㅈ'], 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
    second_sound_list = [
        'ㅏ', 'ㅐ', 'ㅑ', ['shift', 'ㅐ'], 'ㅓ', 'ㅔ', 'ㅕ',
        ['shift', 'ㅔ'], 'ㅗ', ['ㅗ', 'ㅏ'], ['ㅗ', 'ㅐ'],
        ['ㅗ', 'ㅣ'], 'ㅛ', 'ㅜ', ['ㅜ', 'ㅓ'], ['ㅜ', 'ㅔ'],
        ['ㅜ', 'ㅣ'], 'ㅠ', 'ㅡ', ['ㅡ', 'ㅣ'], 'ㅣ'
    ]
    third_sound_list = [
        [], 'ㄱ', ['shift', 'ㄱ'], ['ㄱ', 'ㅅ'], 'ㄴ', ['ㄴ', 'ㅈ'],
        ['ㄴ', 'ㅎ'], 'ㄷ', 'ㄹ', ['ㄹ', 'ㄱ'], ['ㄹ', 'ㅁ'],
        ['ㄹ', 'ㅂ'], ['ㄹ', 'ㅅ'], ['ㄹ', 'ㅌ'], ['ㄹ', 'ㅍ'],
        ['ㄹ', 'ㅎ'], 'ㅁ', 'ㅂ', ['ㅂ', 'ㅅ'], 'ㅅ',
        ['shift', 'ㅅ'], 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]

    first_sound_term = ((ord('힣') - ord('가')))+1 // 19
    second_sound_term = ((ord('깋') - ord('가'))+1) // 21
    third_sound_term = ((ord('갛') - ord('가'))+1) // 28

    def __init__(self):
        pass

    def decomposeSingleChar(self, char: str, return_as_tuple: bool = True) -> typing.Iterable:
        if (ord(char) >= ord('가')) and (ord(char) <= ord('힣')):
            decomposed_char = []
            index = ord(char) - ord('가')
            first_sound_index = index // 28 // 21
            second_sound_index = (index // 28) % 21
            third_sound_index = index % 28
            for letter in self.first_sound_list[first_sound_index]:
                decomposed_char.append(letter)
            for letter in self.second_sound_list[second_sound_index]:
                decomposed_char.append(letter)
            for letter in self.third_sound_list[third_sound_index]:
                decomposed_char.append(letter)
            if (return_as_tuple):
                return tuple(decomposed_char)
            return decomposed_char
        else:
            if (return_as_tuple):
                return tuple(char)
            return list(char)

    def decomposeMultiChar(self, string: str, return_as_tuple: bool = True) -> typing.Iterable:
        decomposed_string = []
        for char in string:
            for letter in self.decomposeSingleChar(char, True):
                decomposed_string.append(letter)
        return decomposed_string


print(decomposer().decomposeMultiChar('왠지 모르게 깍두기가 먹고 싶어.'))
