# Аналитика по рекламным компаниям в кабинете Ozon performance

## Описание проекта:

Сбор статистики в отчет. 

## Развертывание проекта:

1. Создать виртуальное окружение
2. Клонировать текущий репозиторий
3. Установить зависимости

```python3
pip install -r requirements.txt
```
4. Получить ключи в кабинете Ozon perfomance[^1]
5. Создать .env  файл следующей структурой

```
client_id=***@advertising.performance.ozon.ru
client_secret=token
```

### Полезные ссылки:

[^1]: https://performance.ozon.ru/settings/api-keys
[^2]: https://docs.ozon.ru/api/performance/#operation/ListCampaigns
[^3]: https://reqbin.com
[^4]: https://data.page/json/csv