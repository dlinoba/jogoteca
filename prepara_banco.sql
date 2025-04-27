DROP DATABASE IF EXISTS JOGOTECA;
CREATE DATABASE JOGOTECA;
USE JOGOTECA;
CREATE TABLE jogos (id int(11) NOT NULL AUTO_INCREMENT,
		nome varchar(50) NOT NULL,
		categoria varchar(40) NOT NULL,
		console varchar(20) NOT NULL,
		PRIMARY KEY (id)
      ) 
	  ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
CREATE TABLE usuarios (
	  nome varchar(20) NOT NULL,
      nickname varchar(8) NOT NULL,
      senha varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
INSERT INTO usuarios (nome, nickname, senha) VALUES ('Admin', 'ADM','$2b$12$hbq8iNUYziC15idKwyAiiuJwnhWjCvAymS4Gv7cqDjA3egrdjeXxO');
INSERT INTO jogos (nome, categoria, console) VALUES ('Tetris', 'Puzzle', 'Atari'),
													 ('God of War', 'Hack n Slash', 'PS2'),
													 ('Mortal Kombat', 'Luta', 'PS2'),
													 ('Valorant', 'FPS', 'PC'),
													 ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
													 ('Need for Speed', 'Corrida', 'PS2')
													 ;
