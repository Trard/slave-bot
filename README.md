# Slave-bot

Бот для мини-приложения ВК ["Рабы" ("Рабство")](https://vk.com/app7794757).
За использование различных ботов ваш аккаунт может быть обнулен. Делайте всё на свой страх и риск.

## Конфигурация

- Редактируем файл `config.json` через любой текстовый редактор:
  - auth - необходим для авторизации вас в приложении. Инструкция по получению:
    - Открываем [Рабы](https://vk.com/app7794757).
    - Нажимаем `F12` (Для Chromium браузеров).
    - В появившейся панели выбираем вкладку `Network`.
    - Находим кнопку `Filter` (Воронка).
    - В появившемся поле пишем `topUsers`.
    - Нажимаем на вкладку `Рейтинг` в самом приложении с рабами.
    - В панели справа появится поле `topUsers`, нажимаем по нему.
    - Откроется еще одна панель, выбираем в ней вкладку `Headers`.
    - Находим раздел `Request Headers`.
    - Ищем поле `authorization`.
    - Копируем его значение (начинается на **Bearer vk_access_token_settings**)
    - Вставляем скопированный текст в значение `auth` в `config.json` между кавычками.
  - timing - задержка в секундах. За слишком маленькую задержку можно получить временную блокировку.
  - InvisibleSlaves - позволяет покупать невидимых рабов, которые приносят высокую прибыль. (false - выкл, true - вкл). Если будет выключено, будут покупаться дешевые, малоприносящие рабы. Может не работать из-за улучшения античита.
  - buyFetters - покупать ли оковы. (false - выкл, true - вкл)
  - checkBalance - проверять ли баланс. **Обязательно** для minBalance. (false - выкл, true - вкл)
  - maxSlavePrice - максимальная цена раба в рублях.
  - minBalance - минимальное значение баланса в рублях при котором будет работать бот, при балансе меньше минимального бот будет выключаться. **Обязательно** нужно включить checkBalance.
- Сохраняем изменения и закрываем файл.

## Запуск

- Откройте `cmd`.
- Зайдите в папку с распокованным архивом.
- Скопируйте путь к ней в поле сверху. Например **C:\files\slave-bot**.
- Перейдите в нее помощью `cd`. Например **cd C:\files\slave-bot**
- Установите библиотеку requests, если та не установлена, с помощью команды `pip install requests`.
- Запустите бота `python slave-bot.py`.
