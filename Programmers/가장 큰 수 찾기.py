def solution(array):
    max_array = max(array)
    return [max_array, array.index(max_array)]