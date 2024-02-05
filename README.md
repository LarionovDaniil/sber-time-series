# Предсказание временного ряда по данным от Сбербанка
## Задание: оценка объема стабильной части средств на период от  1 месяца до 12

## Стэк
- Pmdarima
- Fastapi
- Streamlit
- Docker
- pickle
- requests
- re
- matplotlib
- pandas
- Pylint

## Результат: 
Веб страница с графиком, на котором при помощи слайдера можно регулировать предсказываемый диапазон времени в месяцах.

## Скачивание весов модели
- После клонирования репозитория необходимо скачать веса модели в backend
https://drive.google.com/file/d/1HSu9QKOUXhwf1-IkkMEAul1-J_zXkABz/view?usp=sharing
## Запуск программы
- находясь в корне, прописать:
```bash
docker compose up --build -d
```
- в браузере написать: `localhost:8501`
