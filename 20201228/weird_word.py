def solution(s):
    answer = []
    for word in s.split(' '):
        new_word = ''
        for i, c in enumerate(word):
            if i%2:
                new_word += c.lower()
            else:
                new_word += c.upper()
        answer.append(new_word)
    return " ".join(answer)
