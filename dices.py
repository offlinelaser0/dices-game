import random


def roll_dice(dices_number=1):
    """Функция, которая симулирует броски костей"""

    try: 
        correct_num_type = int(dices_number)
    except ValueError as error:
         raise Exception(f'У вас произошла ошибка в обработке числа, которое вы ввели {error}')

    # Генерируем случайное число от 1 до 6 (включительно)
    if correct_num_type == 1:
        # Игрок выбрал 1 кость и бросил её
        dice_result = random.randint(1, 6)

        return [dice_result]

    elif correct_num_type == 2:
        # Игрок выбрал 2 кости и бросил их (одновременно)
        dice_result1 = random.randint(1, 6)
        dice_result2 = random.randint(1, 6)

        return [dice_result1, dice_result2]

    elif correct_num_type == 3:
        # Игрок выбрал 3 кости и бросил их (одновременно)
        dice_result1 = random.randint(1, 6)
        dice_result2 = random.randint(1, 6)
        dice_result3 = random.randint(1, 6)

        return [dice_result1, dice_result2, dice_result3]

    else:
        return (
            f"Игра окончена! Вы выбрали неправильное число: {dices_number}"
        )
