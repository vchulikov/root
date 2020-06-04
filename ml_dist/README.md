Требования: 

Скрипт | Требования 
---    |---         
draw_fit.py       | python (2.7.15+), ROOT (6.16/00), numpy (?), math (?) 
pdf_generator.py  | python (2.7.15+), ROOT (6.16/00), numpy (?), math (?)
csv_generator.py  | python (2.7.15+), numpy (?)
model.py          | python (2.7.15+), numpy (?), matplotlib, tensorflow, os
draw_hists.py     | python (2.7.15+), ROOT (6.16/00), numpy (?)
transpose_ds.py   | python (2.7.15+), pandas (?) 

Как запустить:

1. Подбираем функцию плотности распределения по картинке, используя [draw_fit.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/draw_fit.py). Используем необходимую функцию из [Imports.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/Imports.py) (раздел PDF's), выставляем соответствующие хорошему фиту параметры.
2. Берем функцию распределения и параметры, полученные на предыдущем этапе. Подставляем их в [pdf_generator.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/pdf_generator.py), где выбираем количество файлов, которые будут сгенерированы *files_number = ...*. Файлы сохраняются в папку */files/*. Повторяем ту же процедуру для нормы (заболевания). Для правильной нормировки меняем строчку hist1.Scale в [Imports.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/Imports.py)
3. После генерации файлов необходимых распределений, объединяем их в один датасет скриптом [csv_generator.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/csv_generator.py).
4. В конце каждой строки индекс: 0 - для нормы, 1 - для заболевания (или наоборот). Приводим датасет в формат, представленный в примере (папка [datasets](https://github.com/vchulikov/pyroot/tree/master/ml_dist/datasets)). Запускаем скрипт [model.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/model.py), в котором модель учится, а после проверяет свои знания на введенных в строчку с переменной predict_dataset (примеры в скрипте). 

P.S. Чтобы посмотреть полученные гистограммы, используем скрипт [draw_hists.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/additional/draw_hists.py).

P.P.S. Для того, чтобы транспонировать датасет используем скрипт [transpose_ds.py](https://github.com/vchulikov/pyroot/blob/master/ml_dist/additional/transpose_ds.py)
