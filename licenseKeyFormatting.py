def licenseFormat(input,k):
    license = ""
    """
    As the first part of string can have anything (any number < K) we start from the end
    If we start from beginning then we would have to adjust (transfer from first to next and so on till end) 
    the first incase the end has < K
    """
    for i in range(len(input)-1,-1,-1):
        if input[i] != '-':
            license = license + input[i]
            count = count+1
        if count == k and i != 0:
            count = 0
            license = license + '-'

    print(license[::-1])


if __name__ == '__main__':
    input = "5F3Z-2e-9-w"
    division = 4
    licenseFormat(input, division)