# E-Diary Scripts
Special script to fix some values in e-diary [e-diary](https://github.com/devmanorg/e-diary).

## How to use
1. Pull e-diary to your local environment
2. Follow instructions inside e-diary to prepare django environment
3. Run Django shell
```shell
python manage.py shell 
```
4. Copy-paste whole script content.
5. You are ready to go.

## Functions and data from script you may need

### COMMENDATIONS_SAMPLES

Helps you to manage list of possible commendations. You can change text, add new values, remove values you don't need.

Do not forget to reinitialize this list after editing.

### create_commendation

Create commendation for schoolkid for the specifiled subject. It will find last subject lesson and put random value from COMMENDATIONS_SAMPLES.

```shell
create_commendation('Фролов Иван', 'Математика')
```

### remove_chastisements

Remove all chastisement for a schollkid.

```shell
remove_chastisements('Фролов Иван')
```

### fix_marks

Replace all 2 and 3 marks to 5

```python
fix_marks('Фролов Иван')
```
