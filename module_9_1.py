def apply_all_func(int_list, *functions):
    results = {}  # Создаём пустой словарь для результатов
    for func in functions:  # Перебираем переданные функции
        try:
            # Добавляем результат работы функции в словарь, используя имя функции как ключ
            results[func.__name__] = func(int_list)
        except Exception as e:
            results[func.__name__] = f"Ошибка: {e}"  # Обрабатываем возможные ошибки
    return results

# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
