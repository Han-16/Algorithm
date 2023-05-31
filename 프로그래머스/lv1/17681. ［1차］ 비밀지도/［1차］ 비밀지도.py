def solution(n, arr1, arr2):
    scrt_map = []
    for ar1, ar2 in zip(arr1, arr2):
        ar1 = bin(ar1)[2:].zfill(n)
        ar2 = bin(ar2)[2:].zfill(n)
        binary = ""
        for a1, a2 in zip(ar1, ar2):
            binary += max(a1, a2)
        binary = binary.replace("1", "#").replace("0", " ")
        scrt_map.append(binary)
    return scrt_map