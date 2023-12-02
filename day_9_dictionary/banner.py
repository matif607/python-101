def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centred, with ** on either side.
    :param text: The string to print
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border
        on either side.
    :param screen_width: The overall width to print within
        (including the 4 spaces for ** on either side)
    :raises ValueError: if supplied string si too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"string{text} is larger than the specified width {screen_width}")
    if text == '*':
        print('*' * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = f"**{centred_text}**"
        print(output_string)


banner_text('*', 60)
banner_text('Always look on the bright side of the life...', 60)
banner_text('if life seems jolly rotten,', 60)
banner_text("there's something you've forgotten!", 60)
banner_text("and that is to laugh and smile and dance and sing", 60)
banner_text(screen_width=60) # this is known as kwarg
banner_text("When you are feeling in the dumps,", 60)
banner_text("Don't be silly chumps", 60)
banner_text('*', 60)
