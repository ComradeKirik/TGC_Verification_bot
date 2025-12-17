#!/bin/bash



if command -v python3 &> /dev/null; then
    echo "Python 3 уже установлен."
    python3 --version
else
    read -p "Python 3 не найден. Установить? (y/n): " py_answer
    if [[ "$py_answer" == "y" || "$py_answer" == "Y" ]]; then
        echo "Начинаю установку Python 3..."
        sudo apt update
        sudo apt install -y python3 python3-pip

        if command -v python3 &> /dev/null; then
            echo "Python 3 успешно установлен!"
        else
            echo "Ошибка при установке Python."
            exit 1
        fi
    else
        echo "Установка Python отменена. Дальнейшая работа невозможна."
        exit 1
    fi
fi


echo "Проверка aiogram 3..."


if python3.14 -c "import aiogram; from importlib.metadata import version; v=version('aiogram'); exit(0) if v.startswith('3') else exit(1)" &> /dev/null; then
    echo "aiogram 3 уже установлен."
else
    read -p "aiogram 3 не найден. Установить? (y/n): " ai_answer
    if [[ "$ai_answer" == "y" || "$ai_answer" == "Y" ]]; then
        echo "Установка aiogram 3..."


        sudo apt install -y python3-pip


        python3.14 -m pip install "aiogram>=3.0"

        if python3.14 -c "import aiogram" &> /dev/null; then
            echo "aiogram успешно установлен!"
        else
            echo "Ошибка при установке aiogram."
        fi
    else
        echo "Установка aiogram отменена."
    fi
fi

echo "Запуск программы настройки"
python3 settings.py