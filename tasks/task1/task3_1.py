technic = [
("ноутбук", 1500, "Татьяна", "892002001020"),
("смартфон", 500, "Анна", "89220232403"),
("проектор", 300, "Андрей", "89508085230"),
("принтер", 750, "Игорь", "892305605602"),
("планшет", 2300, "Игорь", "892305605602"),
("смартфон", 1000, "Андрей", "89508085230"),
("наушники", 780, "Марина", "89569305467"),
("сканер", 550, "Сергей", "892002001020"),
("планшет", 1200, "Анна", "89220232403"),
("ноутбук", 1100, "Игорь", "892305605602"),
("смартфон", 3500, "Татьяна", "892002001020")]

def new_dict():
    """Вывод словаря с ключём из имени и номера телефона, для значения ключа существует список,
    содержащий поля price и item, содержимое которых соответствует первоначальному списку"""

    technic_dict = dict()
    for i in technic:
        technic_dict.update({f"{i[2]} {i[3]}":[]})
    for a in technic_dict:
        for i in technic:
            n = f"{i[2]} {i[3]}"
            if n == a:
                technic_dict[a].append({f"price: {i[1]} item: {i[0]}"})
    """Более приятное визуально представление закомментировано, чтобы не засорять вывод"""
    # for a in technic_dict:
        #print(f"{a}: {(technic_dict[a])}")

    print(technic_dict)
