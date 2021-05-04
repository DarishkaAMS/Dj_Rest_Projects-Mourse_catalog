# Mourse Course

## Описання
Каталог курсів (мурсів) Mourse Course для проекту Yalantis Python School 
[[_TOC_]]

## Використання

із можливістю:
- перегляду списку мурсів зі сортуванням за датою, пошуком за назвою (у т.ч. слагом) та датою
  -детального ознайомлення з обраним мурсом (окрема сторінка курсу), 
  - додаванням власного мурсу, 
    -радагування та видалення обраного мурсу.

```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```    

## Тестування

```bash
python manage.py test my_mourse
```
Файли у папці my_mourse/tests через дозволяють провести 9 тестів, зокрема: 
- тести для форми MourseForm
- тести для моделі Mourse
- тести для CRUD + list - > my_mourse.urls 
- тести для CRUD + list my_mourse.view 

P.S.Тести написані для звичайних views, тому для їх успішного запуску потрібно в my_mourse.urls перейти з from my_mourse.api_views import... на from my_mourse.views import...
from my_mourse.views import (mourse_create_view,
                                 mourse_delete_view,
                                 mourse_detail_view,
                                 mourse_list_view,
                                 mourse_update_view)

## Розгортання та запуск

## Ліцензія
[MIT](https://choosealicense.com/licenses/mit/)

## Статус проекту
Потребує вдосконалення для якісного розрогтання 