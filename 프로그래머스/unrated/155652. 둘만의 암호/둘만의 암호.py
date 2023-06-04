def solution(s, skip, index):
    decoding = []
    skip = [ord(i) for i in skip]
    s = [ord(i) for i in s]
    
    for i in range(len(s)):
        cnt = 0
        num = s[i]
        while cnt < index:
            if num == ord('z'):
                num = ord('a') - 1            
            if num + 1 in skip:
                num += 1
            else:
                num += 1
                cnt += 1
        decoding.append(num)
    return ''.join(list(map(chr, decoding)))
                