# School-Overflow

The non-commercial product was created by the Autobots team at the Q1 March 2023 school hackathon.

## BackEnd

#### /new_user
- login
- passw

Ответ: True / False / IncorrectValue / Erore

---

#### /question/create
- login         (обязательный)
- passw         (обязательный)
- description   (обязательный)
- text_body     (обязательный)
- label         
- document      

Примечание document хранит файлы в base64 разделённый пробелами.

```python
data = b64encode(data).decode()
data = data+' '+data+' '+data+' '+data
```

Ответ: True / False / IncorrectValue / UnconfirmedEmail / Erore

---

#### /question/(id)/answer (создание ответа)
- login         (обязательный)
- passw         (обязательный)
- text_body     (обязательный)
- document
- id_answ  

Ответ: True / False / IncorrectValue / UnconfirmedEmail / Erore

---

#### /auth (авторизация)
- login         (обязательный)
- passw         (обязательный)

Ответ: True / False / IncorrectValue / UnconfirmedEmail / Erore

---

#### /questions (все вопросы)
- filter        
- - param
- - values        

Ответ: Erore /
```json
"post": {
    "description": "Придумали очень крутую штуку, кто не согласен, то не прав",
    "id": 1,
    "label": "Химия",
    "login": "igorkravchenko",
    "create_at": "2023-03-05"}
```

---

#### /answer/(int:id)/statis (повысить или понизить рейтинг ответа)
- login         (обязательный)
- passw         (обязательный)
- operator (**-**/**+**)     (обязательный)

Ответ: True / False / IncorrectValue / UnconfirmedEmail / Erore

---

#### /question/(id) (конкретный вопрос)

Ответ: Erore / 
```json
{
"0": {"doc": "dmodv_llgytwc7guflbetojyby",
    "id": 1,
    "login": "dmodv",
    "statis": 0,
    "text_body": "Пришлю ему его же скрин АХХАХАХАХ",
    "create_at": "2023-03-05"},
"1": {"doc": "None",
    "id": 2,
    "login": "dmodv",
    "statis": 0,
    "text_body": "Нет я прав, а ты пред несёшь АХАХАХАХХАХАХАХХАХАХАХАХЗХАХАХАХХАХАХАХХАХАХА",
    "create_at": "2023-03-05"},
"post": {
    "description": "Придумали очень крутую штуку, кто не согласен, то не прав",
    "doc": "igorkravchenko_h4wtoj6mvf1cmfyy6hy0",
    "id": 1,
    "label": "Химия",
    "login": "igorkravchenko",
    "text_body": "Мега крутая тема",
    "create_at": "2023-03-05"}
}
```

---

#### /profile
- login         (обязательный)
- passw         (обязательный)

Ответ: False / IncorrectValue / UnconfirmedEmail / Erore / 
```json
{
"0": {"doc": "dmodv_llgytwc7guflbetojyby",
    "id": 1,
    "login": "dmodv",
    "statis": 0,
    "text_body": "Пришлю ему его же скрин АХХАХАХАХ"},
"1": {"doc": "None",
    "id": 2,
    "login": "dmodv",
    "statis": 0,
    "text_body": "Нет я прав, а ты пред несёшь АХАХАХАХХАХАХАХХАХАХАХАХЗХАХАХАХХАХАХАХХАХАХА"},
"post": {
    "description": "Придумали очень крутую штуку, кто не согласен, то не прав",
    "doc": "igorkravchenko_h4wtoj6mvf1cmfyy6hy0",
    "id": 1,
    "label": "Химия",
    "login": "igorkravchenko",
    "text_body": "Мега крутая тема"}
}
```