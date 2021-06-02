Лабораторная:
сделать image контейнера с необходимым ПО для запуска sshd


запустить docker-compose поднять два ssh сервера
	
	docker-compose up --build -d
	
	
продемонстрировать что из одного контейнера можно войти в другой

	по паролю
![linux](https://i.imgur.com/o3782hu.png)
	
		по ключу
	1->2
![linux](https://i.imgur.com/ex7Yoa6.png)
	
	2->1
![linux](https://i.imgur.com/Fl34SyF.png)

	
	выполнить команду
![linux](https://i.imgur.com/e6R2Ya2.png)

	передать файл
![linux](https://i.imgur.com/IGxYbo6.png)


	продемонстрировать простейший обмен данными с помощью утилиты netcat
	
	отправка
![linux](https://i.imgur.com/e98bIte.png)
	
	прием
![linux](https://i.imgur.com/GZcfZKz.png)
