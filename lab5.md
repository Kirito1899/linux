1 Как отобразить 4 последних выполненных команды?  
 history 4  
2 Перевести задание в фоновый режим в bash можно командой  
 command &  
3 Какая комбинация клавиш переключит вас на 4-ю виртуальную консоль?  
 [Ctrl]-[Alt]-[F4]
4 Какая переменная среды содержит путь к домашнему каталогу?  
 HOME
5 Установить в bash переменную MYVAR в качестве системной можно командой?  
 export MYVAR  
6 Какие комбинации клавиш позволят выделить несколько файлов в Midnight Commander?  
 Ctrl+T или Insert  
7 Что выведет на экран этот сценарий?  
#!/bin/bash  
VAR=`echo 'test'`  
VAR2=`echo '$VAR'`  
echo $VAR2  
 ______________________  
 $VAR  
 ______________________  
8 Что выведет на экран это сценарий?  
#!/bin/bash  
cd /etc  
VAR="$PWD"  
if [ -n "$VAR" ]; then  
 echo "$VAR"  
else  
 echo '$VAR'  
fi   
_______________________  
/etc  
_______________________  

9 Что выведет на экран этот сценарий?  
#!/bin/bash  
A=1  
B=2  
if [ $A -eq $B  ]; then  
 echo '$A'  
else  
 echo "$B"  
fi   
_______________________  
2  
_______________________  
 
Задачи:  
 
Задача 1  
Написать скрипт который получает в качестве аргумента 3 значения, a, b,c,d  и рисует прямоугольник  
a - высота прямоугольника  
б - ширина прямоугольника  
с 0/1 - пустой или заполненный  
d - символ из которого следует рисовать  

read file - rectangle

Задача 2  

настроить tmux, научиться запускать, создавать новые pane, делать split pane,  управление мышью, zoom, прокрутка, закрытие pane, detach.  \

 создать новую сессию -  tmux  
 создать сессию командой new-session и задать ей удобное имя - tmux new-session -s losst  
 Создать новое окно Ctrl + B, C  
 Следующее окно Ctrl + B, N
 Увести tmux в фон Ctrl + B, D (detach)
 Предыдущее окно Ctrl + B, P  
 Разделить текущее окно по вертикали Ctrl + B, %  
 Разделить текущее окно по горизонтали Ctrl + B, "  
 
 ПОДДЕРЖКА МЫШКИ 
 vi ~/.tmux.conf  
 set-option -g -q mouse on  
 bind-key -T root WheelUpPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; copy-mode -e; send-keys -M"  
 bind-key -T root WheelDownPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; send-keys -M"  
 ~/.tmux.conf  
 
 zoom -  Ctrl + b, а затем z  
 
 
