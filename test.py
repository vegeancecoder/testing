def test(num):
    if num ==1:
        return num
    return num+test(num)