# School-Overflow

The non-commercial product was created by the Autobots team at the Q1 March 2023 school hackathon.

## BackEnd

#### /new_user
- login
- passw

#### /posts/create
- login         (обязательный)
- passw         (обязательный)
- description   (обязательный)
- text_body     (обязательный)
- label         (не обязательный)
- document      (не обязательный)

Примечание document хранит файлы в base64 разделённый пробелами.

```python
data = b64encode(data).decode()
data = data+' '+data+' '+data+' '+data
```

Ответ: True/False/IncorrectValue/Erore

#### /posts/answer
- login         (обязательный)
- passw         (обязательный)
- post_id       (обязательный)
- text_body     (обязательный)
- document      (не обязательный)

Ответ: True/False/IncorrectValue

#### /posts
- login         (обязательный)
- passw         (обязательный)
- filter        (не обязательный)
- - param
- - values        

Ответ: True/False/IncorrectValue/Erore

#### /posts/question
- login         (обязательный)
- passw         (обязательный)
- post_id       (обязательный)

Ответ: False/IncorrectValue/Erore/
```json
{
0: {doc: "dmodv_llgytwc7guflbetojyby",
    id: 1,
    login: "dmodv",
    statis: 0,
    text_body: "Пришлю ему его же скрин АХХАХАХАХ"},
1: {doc: "None",
    id: 2,
    login: "dmodv",
    statis: 0,
    text_body: "Нет я прав, а ты пред несёшь АХАХАХАХХАХАХАХХАХАХАХАХЗХАХАХАХХАХАХАХХАХАХА"},
"post": {
    description: "Придумали очень крутую штуку, кто не согласен, то не прав",
    doc: "igorkravchenko_h4wtoj6mvf1cmfyy6hy0",
    id: 1,
    label: "Химия",
    login: "igorkravchenko",
    text_body: "Мега крутая тема"}}
```

#### /profile
- login         (обязательный)
- passw         (обязательный)

Ответ: False/IncorrectValue/Erore