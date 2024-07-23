-- CREATING DATABASE FOR QUIZGAME

CREATE DATABASE quizgame;

USE quizgame;

-- CREATE TABLE quizdata(
--     sno INT AUTO_INCREMENT PRIMARY KEY, 
--     question VARCHAR(255), 
--     optionA VARCHAR(100),
--     optionB VARCHAR(100),
--     optionC VARCHAR(100),
--     optionD VARCHAR(100),
--     correct_ans VARCHAR(1)
-- )

DROP TABLE quizdata;
DROP TABLE login_info;

SELECT * FROM user_info;