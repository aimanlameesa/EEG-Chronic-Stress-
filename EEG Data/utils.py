def get_filenames_in_path(path):
    from os import walk
    _, _, filenames = next(walk(path))
    return filenames

def balanced_latin_squares(n):
    l = [[((j//2+1 if j%2 else n-j//2) + i) % n + 1 for j in range(n)] for i in range(n)]
    if n % 2:  # Repeat reversed for odd n
        l += [seq[::-1] for seq in l]
    return l