Нужно написать мини app, в котором:
Распарсить два 2 .csv файла (ссылки прилагаются) (Products, Reviews), данные сохранять в базу (использовать Postgres, соотношения one-to-many или many-to-many на выбор). Парсинг и сохранение в базу можно реализовать консольной командой.

Products https://docs.google.com/spreadsheets/d/1roypo_8amDEIYc-RFCQrb3WyubMErd3bxNCJroX-HVE/edit#gid=0
Reviews https://docs.google.com/spreadsheets/d/1iSR0bR0TO5C3CfNv-k1bxrKLD5SuYt_2HXhI2yq15Kg/edit#gid=0


На основе Flask создать API endpoint (GET), который будет возвращать данные в формате json следующего содержания:
По id товара отдавать информацию по этому товару (ASIN, Title) и Reviews этого товара с пагинацией.
Желательно создать кеширование для GET endpoint.

Создать второй API endpoint (PUT), который будет писать в базу данных новый Review для товара (по id).



Требования:
- Python 3
- Flask
- pep 8
- Postgres DB
- requirements.txt
