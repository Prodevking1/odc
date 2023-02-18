magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
    for i in range(len(magician_names)):
        print(magician_names[i])


def make_great():
    for i in magician_names:
        i = i + " the Great"
        print(i)


make_great()
