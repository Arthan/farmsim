def get_int(text, min, max, empty=False):
    nr = input(text)
    if empty and nr == '':
        return None
    if not nr.isdigit() or not (max >= int(nr) >= min):
        print('To nie jest prawidłowy wybór!')
        return get_int(text, min, max)
    return int(nr)
