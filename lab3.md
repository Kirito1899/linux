#Lab 3
1. Третье поле в файле /etc/passwd содержит?  
  Идентификатор пользователя - UID
2. Что такое Теневые файлы паролей?  
 Файлы, в которых хранится информация в защищённом виде (доступны только для root пользователя)  
/etc/shadow - информация о пользователях  
/etc/gshadow - информация о группах  
	
3. Какой пользователь имеет UID и GID равными 0?  
	root
	
4. Как сменить активный идентификатор группы?  
	newgrp 

5. Как сменить пароль пользователя?  
	passwd user
	
6. Как установить время истечения пароля пользователя?  
	chage -d date

7. изменить права на файл в символьном и абсолютном режиме  
* r w x r- - r - -  
	chmod u+rwx,go+r-wx file_name  
  chmod 744 file_name  
* r - - - w- - - x  
	chmod u=r,g=w,o=x file  
	chmod 421 file
* \- - x - w - r - -  
	chmod u=x,g=w,o=r file  
	chmod 124 file  
	
8. Что означает строка -wx-w---- ?  
	Владелец имеет права на запись и исполнение  
	Группа имеет права на запись  
	Никто другой не имеет права выполнять никакие действия  

9. Что означает строка прав доступа r--r-xrwx для каталога?  
	Владелец имеет права на чтение  
	Группа имеет права на чтение и вход в каталог  
	Остальные имеют права на чтение, запись и вход в каталог  

10. Какой командой установить права -wx--x-w- на файл?  
	chmod 312 file
11. Какой командой в абсолютном режиме установить права rw---xr-- на файл?  
	chmod 614 file
	
12. Какая команда в абсолютном режиме разрешит полный доступ к файлу для всех?  
	chmod 777 file
	
13. Какая команда установит такие права на каталог, что удалять файлы из него смогут только владельцы этих файлов?  
	chmod +t directory