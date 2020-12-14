Запуск: docker_compose up
Эндпойнты апи:
GET /<product_id>/ Получить товар c id = product_id

PUT /<product_id>/ Добавить рецензию в товар c id=product_id, (необходимы поля рецензии "review_title"и "review_text" в теле запроса)
