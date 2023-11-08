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

## Результат: 
Веб страница с графиком, на котором при помощи слайдера можно регулировать предсказываемый диапазон времени в месяцах.

## Запуск программы
- находясь в корне, неободимо прописать:
```bash
docker compose up --build -d
```
- открыть браузер и в поисковой строке написать: `localhost:8501`
