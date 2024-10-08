# Lesson_17_18
## Як встановити виртуальне середовище. Парсінг пдф файлів
Віртуальне середовище для Python дозволяє створити ізольований простір для вашого проекту, де можна встановлювати специфічні версії пакетів, не впливаючи на глобальну установку Python.

Відкрийте командний рядок (Command Prompt). Для цього натисніть клавішу Windows і введіть "cmd", потім натисніть Enter. Або, якщо ви користувач Лінукс (що краще), то відкрите термінал, настиснувши комбінацію клавіш _cntrl + alt + T._ 

Переконайтеся, що у вас встановлена остання версія `pip` (менеджера пакетів для Python). Введіть у командному рядку наступну команду:


`python -m pip install --upgrade pip`

Встановіть пакет `virtualenv`, який допоможе вам створювати віртуальні середовища. Введіть у командному рядку:

`pip install virtualenv`

Перейдіть до папки, де ви хочете створити проект. Використовуйте команду `cd` для переходу між папками. Наприклад, щоб перейти до папки "Documents\MyProject":

`cd Documents\MyProject`

Створіть віртуальне середовище, ввівши:

`python -m virtualenv venv`

Тут `venv` - це ім'я папки, де буде зберігатися віртуальне середовище. Ви можете назвати її як завгодно.
Щоб активувати віртуальне середовище, виконайте наступну команду:

`.\venv\Scripts\activate`

Для лінукс систем:

`source venv/bin/activate
`
Після активації ви побачите ім'я вашого віртуального середовища у командному рядку, наприклад `(venv)`.
Тепер ви можете встановлювати пакети, які будуть ізольовані у вашому віртуальному середовищі. Наприклад, щоб встановити `pdfx` та `pprint`, введіть:

`pip install pdfx`

Щоб вийти з віртуального середовища, введіть команду:
deactivate

Щоб повторно активувати ваше віртуальне середовище в майбутньому, перейдіть до папки проекту та введіть команду активації:

`.\venv\Scripts\activate`

або для Лінукс:

`source venv/bin/activate
`
