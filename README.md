# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в репозиторий случайно, то вам не удастся его запустить при отсутствии доступа к БД, но вы можете свободно использовать код вёрстки или посмотреть на реализацию запросов к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
В переменной окружения SECRET_KEY хранится пароль от БД. Для работы потребуется создать файл .env и задать в нём значение переменной SECRET_KEY, например: 
```
export SECRET_KEY = OPEN_BASE
```
Переменная DEBUG отвечает за отладочный режим. Настройка DEBUG в .env файле включит отладочный режим при: 
```
export DEBUG = True 
```
И наоборот, выключится при значении False.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).