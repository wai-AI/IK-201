#!/bin/bash

# Функция для проверки интернет-соединения
check_internet() {
    ping -c 1 google.com > /dev/null 2>&1
    return $?
}

python bot.py &

# Основной код скрипта

while true; do
    if check_internet; then
        #echo "Подключение активно"
        sleep 3
    else
        echo "Интернет соединение отсутствует. Перезапуск процесса..."

        pkill python

        sleep 3
        python bot.py &
    fi
done
