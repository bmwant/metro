 
DROP TABLE IF EXISTS `ref_errors`;
CREATE TABLE `ref_errors` ( ErrorCode INTEGER, ErrorName VARCHAR(50) );
DELETE FROM 'ref_errors';
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 0,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 1,'недостатньо ресурсiв' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 2,'невiрний срок дiї' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 3,'стороння картка' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 4,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 5,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 6,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 7,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 8,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 9,'помилка вiдсутня' );
INSERT INTO ref_errors ( ErrorCode, ErrorName ) VALUES ( 10,'помилка вiдсутня' );

DROP TABLE IF EXISTS `ref_events`;
CREATE TABLE `ref_events` ( EventCode INTEGER, EventName VARCHAR(50) );
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








