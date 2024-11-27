import nmap

def scan_host(host, port_range="1-1024"):
    nm = nmap.PortScanner() # Объект для работы с nmap

    print(f"Сканируем {host} на порты {port_range}...") # Скан хоста с заданным диапазоном портов
    nm.scan(host, port_range)

    if nm.all_hosts(): # Инфа о хосте
        for host in nm.all_hosts():
            print(f"\nХост: {host}")
            print(f"Состояние хоста: {nm[host].state()}")
            print("Открытые порты:")
            for proto in nm[host].all_protocols():
                print(f"  Протокол: {proto}")
                ports = nm[host][proto].keys()
                for port in ports:
                    print(f"    Порт: {port}, Статус: {nm[host][proto][port]['state']}")
    else:
        print("Хост не найден.")

host_to_scan = input("Введите IP-адрес или домен для сканирования: ")
port_range = input("Введите диапазон портов (по умолчанию 1-1024): ") or "1-1024"

scan_host(host_to_scan, port_range)