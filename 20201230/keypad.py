def solution(numbers, hand):
    def get_position(n):
        pos = [(3, 1),
               (0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)]
        return pos[n]

    answer = []
    left, right = (3, 0), (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            left = get_position(number)
            answer.append("L")
        elif number in [3, 6, 9]:
            right = get_position(number)
            answer.append("R")
        else:
            number_pos = get_position(number)
            left_distance = abs(number_pos[0] - left[0]) + abs(number_pos[1] - left[1])
            right_distance = abs(number_pos[0] - right[0]) + abs(number_pos[1] - right[1])
            if left_distance < right_distance:
                left = number_pos
                answer.append("L")
            elif right_distance < left_distance:
                right = number_pos
                answer.append("R")
            else:
                if hand == 'left':
                    left = number_pos
                    answer.append("L")
                else:
                    right = number_pos
                    answer.append("R")
    return "".join(answer)
