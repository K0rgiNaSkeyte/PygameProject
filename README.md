# Техническое задание (ТЗ) на создание демонстрационной версии 2D RPG игры.

## 1. Цель проекта.
Создание простой игры на клеточном поле с тремя уровнями. Создание главного меню, экрана проигрыша, выигрыша, настроек, итогового счёта, боя. Пользователь может сохранять прогресс прохождения и загружать. Создание системы очков.

## 2. Основные функции приложения.

### 2.1 Главное меню.
Меню должно содержать пять(четыре) кнопки: 
	- "Начать игру", которая позволяет пользователю начать игру с самого начала;
	- "Загрузить игру", которая позволяет пользователю продолжить прохождение игры с сохраненного положения;
	- "Настройки", которая позволяет изменить громкость музыки и эффектов;
	- "Выход", которая закрывает окно игры;
	- "Рекорд", которая отображает взятые из таблицы номера успешных прохождений игры и очки, набранные игроком.

### 2.2 Игровой процесс.
- Должны быть созданы три игровых уровня. Переход с уровня на уровень осуществляется с помощью дверей, расположенных на краю клеточного поля.
- Передвижение по клеточному полю осуществляется с помощью клавиш "WASD"
- На холсте в момент передвижения, отрисовывается текущее количество очков за прохождение, номер прохождения.
- Есть несколько типов врагов, разного уровня сложности. При столкновении персонажа и врага осуществляется отрисовка экрана боя (см. 2.3). При проигрыше отрисовывается соответствующий экран, с кнопками "Вернуться в главное меню", или "Загрузить сохранённую игру". При выигрыше персонаж передвигается на место врага, клетка перестаёт быть "враждебной", становясь обычным полем. Игра продолжается с сохранением прогресса.
- Когда персонаж доходит до конца третьего уровня, отрисовывается экран выигрыша с кнопками "Выход" и "Вернуться в главное меню". Накопленные в процессе прохождения игры очки и номер успешного прохождения сохраняются в таблицу базы данных.

### 2.3 Бой.
- Бой осуществляется путём поочерёдных действий игрока и противника. На экране при этом всегда отрисовывается спрайт и имя противника и портрет и имя героя с простыми анимациями, показатели здоровья и маны противника и героя. Первый ход всегда за игроком. По-окончании боя, показатель жизни персонажа полностью восстанавливается. В начале боя игрок имеет случайный показатель очков маны от 10 до 20. Бой осуществляется с помощью трёх кнопок: 
	- "Атака", из количества очков здоровья врага отнимается случайное число от 1 до 15.
	- "Восстановление", из количества очков маны отнимается случайное число от 1 до 3, к показателю здоровья игрока прибавляется случайное число от 1 до 15.
	- "Восстановление маны", к количеству очков маны прибавляется случайное число от 1 до 5.

#### 2.3.1 Очки боя.
- Со старта боя ведётся подсчёт ходов игрока. 
- Формула отсчёта очков, получаемых за бой:
	- n - число ходов игрока
	- m - число потерянного противником здоровья
	- k - переменная величина (см 2.3.2)
	- P1 - итоговое число очков за бой.
	- P0 - число очков до начала сражения.
	- P1 = (m - (n/k*m)) + P0
- P1 перезаписывается в таблицу базы данных.

#### 2.3.2 Переменная величина.
Переменная величина принимает значения 10, 100, 1000.. В зависимости от n. Если n >= k, то k*10.

### 2.4 Очки.
- За завершение игры добавляется 500 очков к текущему прохождению.
- Очки за каждое прохождение можно посмотреть в виде таблицы, которая отрисовывается на новом холсте при нажатии на кнопку "Счёт".
- Игрок может загрузить уже пройдённую игру и увеличить количество очков. За загрузку и повторное прохождение до конца игры 500 очков не начисляются.
- Игрок теряет 10 очков если "Восстановление маны" во время боя было нажато 10 раз.
- ...

### 2.5 Настройки.
- Должно быть реализовано минимум два подписанных ползунка, отвечающих за громкость музыки и звуковых эффектов. По умолчанию громкость музыки и звуковых эффектов принимают максимальное значение.
- К настройкам должен быть доступ с меню паузы.
- В настройках есть кнопка "Сброс прогресса", которая очищает базу данных и удаляет сохранения.

### 2.6 Меню паузы.
- Меню паузы вызывается нажатием клавиши "ESC"
- В меню паузы есть пять кнопок: 
	- "Вернуться в игру", которая закрывает меню паузы.
	- "Счёт" 
	- "Загрузить игру"
	- "Настройки"
	- "Выход", которая возвращает игрока в главное меню не сохраняя прогресс прохождения.

## 3. База данных.

### 3.1 Данные сохранений.
- Где хранятся: В базе данных (SQLite).
- Какие данные: положение игрока, состояние уровней и врагов на них, текущий счёт, название сохранения.

### 3.2 Данные счётов игр.
- Где хранятся: В базе данных (SQLite).
- Какие данные: порядковый номер (начинается с единицы), счёт

## 4. Чек-лист.
- [X] v. 0.0.0
- [ ] Реализована база данных
- [ ] Классы
- [ ] Создано главное меню
- [ ] Создано окно настройки
- [ ] Создано окно счёта
- [ ] Созданы уровни
- [ ] Создан экран боя
- [ ] Создан экран поражения
- [ ] Создан экран победы
- [ ] collision
- [ ] 500 строк кода
- [ ] Анимация
- [ ] Пояснительная записка
- [ ] Презентация
