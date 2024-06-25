import os


def remove_database(db_name = str):
    os.remove(db_name + ".txt")


def create_file(file_name = str, encoding = str):
    with open(file_name, 'a', encoding=f'{encoding}') as file:
        file.close()
        return "file created"


def decode_list(initial_words = list, separation = str):
    line = ""
    for word in initial_words:
        line += f"{word}{separation}"
    return line[:-1]
    

def create_db(name = str, separation = str, encoding = str, initial_words = list):
    file_db_name = name + ".txt"
    if os.path.exists(file_db_name):
        return
    if len(name) > 0:
        if len(separation) > 0:
            file_db_name = name + ".txt"
            response = create_file(file_name=file_db_name, encoding=encoding)
            if response == 'file created':
                start = decode_list(initial_words=initial_words, separation=separation)
                with open(file_db_name, 'a', encoding=f'{encoding}') as file:
                    file.write(start)
                    file.close()
            else:
                return "file creation error"
        else:
            return "Error, separation must be greater than 1 character"
    else:
        return "Error, name must be greater than 1 character"


def get_line_of_user(user = int, db_name = str, encoding = str):
    id = str(user)
    with open(f"{db_name}.txt", 'r', encoding=f'{encoding}') as db:
        for line in db:
            if line:
                if id in line:
                    return line
    return None


def check_user_in_database(db_name = str, encoding = str, user = int):
    id = str(user)
    with open(f'{db_name}.txt', 'r', encoding=f'{encoding}') as db:
        for line in db:
            if line:
                if id in line:
                    return True
    return False


def get_struct_db(db_name = str, encoding = str):
    file_name = db_name + ".txt"
    with open(file_name, 'r', encoding=f'{encoding}') as file:
        for line in file:
            if line:
                return line.strip()
            break



def redata(db_name = str, encoding = str, user = int, re_data = dict, separation = str, part_id = int):
    itd = ""
    re_data_id = 0
    file_name = db_name + ".txt"
    id = str(user)
    itog_line = ""
    struct = get_struct_db(db_name=db_name, encoding=f'{encoding}')
    strct = struct.split(separation)
    with open(file_name, 'r', encoding=f'{encoding}') as db:
        for line in db:
            if line:
                parts = line.strip().split(f'{separation}')
                if parts[part_id] == str(user):
                    itog_line += line.strip()
                    break
    for w in strct:
        if w in re_data:
            itd += re_data[w]
            break
        else:
            re_data_id += 1
     
    file_path = file_name
    updated_lines = []
    # Чтение данных из файла и обновление нужной строки
    with open(file_path, 'r', encoding=f'{encoding}') as file:
        for line in file:
            if line:
               parts = line.strip().split(separation)
               if parts[part_id] == str(user):
                  parts[re_data_id] = itd # Заменяем старое значение баланса на новое
                  updated_lines.append(f'{separation}'.join(parts) + "\n")
               else:
                  updated_lines.append(line)

    # Запись обновленных данных обратно в файл
    with open(file_path, 'w', encoding=f'{encoding}') as file:
        for line in updated_lines:
            file.write(line)


def add_data(separation = str, struct = str, data = dict, db_name = str, encoding = str):
    itog_line = ""
    file_name = db_name + ".txt"
    res = struct.split(f'{separation}')
    for w in res:
        if w in data:
            word = data[w]
            itog_line += f"{word}{separation}"
    itl = itog_line[:-1]
    with open(file_name, 'a', encoding=f'{encoding}') as db:
        db.write(f"{itl}\n")
