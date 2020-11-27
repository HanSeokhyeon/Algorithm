from collections import Counter


def solution(s):
	s_counter = Counter(list(s.lower()))
	return s_counter['p'] == s_counter['y']
