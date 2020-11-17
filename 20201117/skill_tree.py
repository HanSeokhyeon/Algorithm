def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        is_skill_tree = True

        skill_idx = [100] * len(skill)
        skill_idx[0] = skill_tree.find(skill[0])
        if skill_idx[0] == -1:
            skill_idx[0] = 100

        for i, sk in enumerate(skill[1:]):
            skill_idx[i + 1] = skill_tree.find(sk)
            if skill_idx[i + 1] == -1:
                skill_idx[i + 1] = 100
            if skill_idx[i] > skill_idx[i + 1]:
                is_skill_tree = False
                break

        if is_skill_tree:
            answer += 1

    return answer
