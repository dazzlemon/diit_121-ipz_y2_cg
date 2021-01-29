from factories import ButtonHandledFactory

def button_handled_stack(size, manager, buttons, start):
    bhf = ButtonHandledFactory(
        size,
        manager
    )
    btns = []

    for i, btn in enumerate(buttons, start = 0):
        btns.append(bhf.make(
            pos = (start[0], start[1] + size[1] * i),
            text = btn[0],
            handle = btn[1]
        ))

    return btns
