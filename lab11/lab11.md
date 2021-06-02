Лабораторная:
сделать image контейнера с необходимым ПО для запуска sshd


запустить docker-compose поднять два ssh сервера
	
	docker-compose up --build -d
	
![image](https://user-images.githubusercontent.com/70812795/120493631-8eba7700-c3d4-11eb-9aac-e5fc56e26a7e.png)

продемонстрировать что из одного контейнера можно войти в другой

	по паролю
![image](https://user-images.githubusercontent.com/70812795/120496079-b4e11680-c3d6-11eb-8f0f-a177af7c8155.png)
![image](https://user-images.githubusercontent.com/70812795/120496434-fec9fc80-c3d6-11eb-9cc0-990fa5170bf4.png)

		по ключу
	1->2
![image](https://user-images.githubusercontent.com/70812795/120497415-d1318300-c3d7-11eb-8773-1bbeb8dbc68f.png)
	
	2->1
![image](https://user-images.githubusercontent.com/70812795/120497210-a5160200-c3d7-11eb-919e-73077538cb2e.png)

	
	выполнить команду
![image](https://user-images.githubusercontent.com/70812795/120497678-0d64e380-c3d8-11eb-8a0a-ee7022d3a638.png)

	передать файл
![image](https://user-images.githubusercontent.com/70812795/120500459-4a31da00-c3da-11eb-82ce-f9048baf8982.png)


	продемонстрировать простейший обмен данными с помощью утилиты netcat
	
	отправка и прием
![image](https://user-images.githubusercontent.com/70812795/120501126-caf0d600-c3da-11eb-9f87-42be9b405245.png)
