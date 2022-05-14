def solution(strings, n):
    
    dict_strings = {string : i for i, string in enumerate(strings)}

    dict_strings2 = sorted(str(dict_strings.items())[n])
    
    return dict_strings2

print(solution(["sun", "bed", "car"], 1))