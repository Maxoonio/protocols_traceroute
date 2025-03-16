from traceroute import traceroute
from parser import result_function

if __name__ == '__main__':
    target = input("Введите доменное имя или IP-адрес: ").strip()
    print("Выполняется трассировка...")
    results = traceroute(target)
    print(f"Трассировка завершена. Найдено {len(results)} IP-адресов.")

    print("Форматирование и сохранение результатов...")
    result_function(results)
    print("Результаты сохранены в файл out.txt.")