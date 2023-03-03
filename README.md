# School-Overflow

The non-commercial product was created by the Autobots team at the Q1 March 2023 school hackathon.

## BackEnd

#### /new_user
- login
- passw

#### /posts/create
- login
- passw
- description
- text_body
- label
- document

Примечание document хранит файлы в base64 разделённый пробелами.

```python
data = b64encode(data).decode()
data = data+' '+data+' '+data+' '+data
```