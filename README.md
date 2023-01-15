# VKinder

VKinder - чат-бот для знакомств в социальной сети ВКонтакте


## Принцип работы
Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок.

Используя данные из VK, нужно сделать сервис намного лучше, чем Tinder, а именно: чат-бота "VKinder". Бот должен искать людей, подходящих под условия, на основании информации о пользователе из VK:

Бот анализирует:
- возраст
- пол
- город
- семейное положение

У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии профиля и отправлять их пользователю в чат вместе со ссылкой на найденного человека. Популярность определяется по количеству лайков и комментариев.


## Входные данные
Никнейм пользователя для которого мы ищем пару или его id в VK.
Если информации для поиска в профиле недостаточно, данные дополнительно запрашиваются у пользователя в чате.


## Настройки
Перед запуском бота необходимо добавить в settings.py токен группы и токен пользователя для работы с API VK.
Для старта приложения нужно настроить Longpoll внутри группы.
