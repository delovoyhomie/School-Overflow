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

#### /posts/answer
- login         (обязательный)
- passw         (обязательный)
- post_id       (обязательный)
- text_body     (обязательный)
- document      (не обязательный)

#### /posts
- login         (обязательный)
- passw         (обязательный)
- label         (не обязательный)

#### /posts/question
- login         (обязательный)
- passw         (обязательный)
- post_id       (обязательный)