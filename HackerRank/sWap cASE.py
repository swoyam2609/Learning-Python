def swap_case(s):
   for i in s:
        if i.isupper():
            print(i.lower(), end='')
        else:
            print(i.upper(), end='')
    return ""
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)