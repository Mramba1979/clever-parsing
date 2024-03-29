# Задача
:books: Спарсить данные карточек товаров с сайта издательства Clever.

## Инструменты
* Python 3
* Pandas
* Excel

# Результаты
Бот собрал все карточки товаров в интернет-магазине.
* **Всего карточек 790.**
* **Время выполнения парсинга ~20 секунд**.

Формат записи:

title | price | author | url
--- | --- | --- | ---
Большая арт-мастерская | 3 315 | Нет автора | https
Робосчёт | 1670 | Карякина О.      | www

## Меры центральной тенденции
* count	790
* mean	562,7075949
* std	358,9990652
* min	50
* 25%	325
* 50%	465
* 75%	655
* max	3315

## Топ авторов
| Имя автора    | Количество совпадений |
|:-------------:|:-------------:|
|Автор не указан|279|
|Уткина О.      |23|
|Скоттон Р.     |18|
|Данилова Л.    |14|
|Узорова О. В.  |12|
|Попова Е.      |11|
|Бессон А.      |10|
|Мальцева И.    |10|

Остальные авторы имеют меньше 10 совпадений.

**Итого авторов 217**

## График распределения цен
![Распределение по частоте цен](https://github.com/Drewleks/clever-parsing/blob/master/price_plot.png "Распределение по частоте цен")

## Возможные ошибки
Ошибка в карточке товара [15 книжек-кубиков. Русский язык](https://www.clever-media.ru/CleverProducts/Books/book_3238/).

Под блоком изображений упоминается блок из другой книги:
> Гид для родителей
> «Оружие Победы. Подробная энциклопедия военного оружия. 1941-1945 гг.»

## Данные о компании
* Статус: Действующее предприятие
* Дата регистрации: 08.09.2006 
* Среднесписочная численность работников: 90

### Доходы и расходы по обычным видам деятельности — 2017
* Выручка	699 523 000,00
* Себестоимость продаж	181 011 000,00
* Валовая прибыль (убыток)	518 512 000,00
* Коммерческие расходы	87 686 000,00
* Управленческие расходы	238 870 000,00
* Прибыль (убыток) от продаж	191 956 000,00
