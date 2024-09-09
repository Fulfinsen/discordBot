from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        print("Don't be shy")
    elif 'hello' in lowered:
        return 'Hello there'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice (['I do not understand',
                        'Tell me again please!'])
