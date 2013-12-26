.echo OFF
CREATE TABLE `ref_events` ( EventCode INTEGER, EventName VARCHAR(50) );
BEGIN TRANSACTION;
DELETE FROM 'ref_events';
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 220,'Інкасація' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 206,'Запис ресурсу' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 212,'Операція з гаманцем' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 1, 'Включення живлення' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 2, 'Вхід до технологічного меню' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 3, 'Завершення роботи' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 4, 'Вхід до меню інкасування' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 5, 'Перегляд історії' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 6, 'Відкриття пристрою (спрацював датчик )' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 7, 'Закриття пристрою (спрацював датчик )' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 8, 'Вилучення бункеру' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 9, 'Встановлення бункеру' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 15, 'Додана купюра)' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 17, 'Запуск ПЗ(№ версії' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 18, 'Встановлена картка' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 19, 'Завершення роботи з карткою' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 28, 'Купюру повернуто' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 29, 'Прийнято купюру' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 39, 'Друк службового чеку' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 42, 'Обслуговування пристрою' );
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 43, 'Закінчення обслуговування');
INSERT INTO ref_events ( EventCode,EventName ) VALUES ( 45, 'Перевірка бази даних');
COMMIT;
.exit






