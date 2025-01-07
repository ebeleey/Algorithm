def solution(s):
    if len(s) == 1:
        return 1

    answer = 0
    compressed_len = [0]*(len(s)//2)
    for size in range(1, len(s)//2 + 1):
        compressed_s = ""
        previous_block = s[:size]
        count = 1
        for i in range(size, len(s), size):
            block = s[i: i+size]
            if previous_block == block:
                count += 1
            else:
                if count > 1:
                    compressed_s += str(count) + previous_block
                else:
                    compressed_s += previous_block
                count = 1
            previous_block = block

        if count > 1:
            compressed_s += str(count) + previous_block
        else:
            compressed_s += previous_block
        compressed_len[size-1] = len(compressed_s)
    answer = min(compressed_len)

    return answer