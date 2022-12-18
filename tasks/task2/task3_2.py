
def list_to_list():
    first_list = ["ddsgdsgdshh", "abcdhi", "effghg", "sdfsdgsdg", "fgfghfhfg", "fdsghjghjdshh", "fdsgdghjghksg"]
    final_list = []
    tab_list = []
    sort_list = []

    """Не совсем понял условие и сделал несколько вариантов
    В этом варианте длина строки подгоняется под наибольшую, повторяющиеся символы заменяются подчёркаиваниями,
    а символы сдвигаются влево"""

    for i in first_list:
        for b in i:
            i = i.replace(b, "_", i.count(b) - 1)
        tab_list.append(i)
    for i in tab_list:
        empty = ""
        if "_" in i:
            empty = "_" * i.count("_")
            i = i.replace("_","",i.count("_"))
            i = i+empty
        else:
            pass
        sort_list.append(i)
    for i in sort_list:
         final_list.append(i) if len(i) == max(first_list) else final_list.append(i+("_" * (len(max(first_list, key=len)) - len(i))))

    print(f"Вариант 1: {final_list}")


    """Вариант номер два - возвращает список строк без повсторяющихся символов, но не сдвигает их"""
    tab_list =[]
    for i in first_list:
        for b in i:
            i = i.replace(b, "_", i.count(b) - 1)
        tab_list.append(i)
        final_list = []
        for i in tab_list:
              final_list.append(i) if len(i) == max(first_list) else final_list.append(i+("_" * (len(max(first_list, key=len)) - len(i))))

    print(f"Вариант 2: {final_list}")
