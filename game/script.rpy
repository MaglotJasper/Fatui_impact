# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

define barbara = Character('Барбара', color="#c8ffc8")
define jean = Character('Джин', color="#c8ffc8")
define lumin = Character('Люмин', color="#c8ffc8")
define main_spy = Character('main_spy', color="#c8ffc8")
define mona = Character('Мона', color="#c8ffc8")
define sucrose = Character('Сахароза', color="#c8ffc8")
define tartaglia = Character('Тарталья', color="#c8ffc8")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    mona "Хочу деняк"

    mona "Многа деняк"

    return
