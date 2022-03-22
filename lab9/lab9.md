Что такое RAID для каких целей он используется?  
Raid массивы (рейд массивы) – это массивы жестких дисков, работающих в связке для увеличения надежности хранимых данных, улучшения производительности, скорости чтения и записи данных. Рейд массивы обеспечивают высокую эффективность использования памяти, в отличие от одного жесткого диска в системе.

Объясните различия между Raid0, Raid1 и Raid5? Плюсы минусу, принцип.  
RAID 0
Такая конфигурация позволяет связать несколько HDD в один, суммируя общий объем подключенных дисков. Винчестеры присоединяются последовательно и воспринимаются системой как один диск. Например, возьмем 3 диска по 1 Тб и создадим из них Raid 0. Операционная система будет воспринимать массив как один жесткий диск суммарным объемом 3 Тб, который позволяет выполнять функции чтения и записи одновременно на нескольких дисках. Что касается скорости чтения и записи, то тут все просто – количество жестких дисков в этой конфигурации умножается на существующую скорость. То есть скорость чтения увеличивается во столько раз, сколько дисков установлено в массиве.  
Минусом данного массива можно назвать зависимость сохранения данных от всех накопителей в связке. Если “умирает” один жесткий диск, то весь массив данных теряется.   
RAID 1  
Суть этого зеркального массива заключается в создании полного дубликата одного диска. То есть, если у вас 4 диска по 1 Тб, то в итоге вы получаете 2 Тб реального объема + 2 запасных Тб для восстановления данных. Используется для надежного сохранения информации, но прибавки к скорости чтения и записи не дает никакой. Такой массив актуален для тех, кто хранит ценную информацию, потерять которую смерти подобно.  

RAID 5  
Одна из наиболее простых и безопасных конфигураций рейд массива. Смысл его стоит в следующем – несколько жестких дисков объединяются в Raid 0, а один диск (или больше, в зависимости от количества HDD в связке) остается для хранения контрольной суммы данных других дисков для последующего восстановления на случай, если один из дисков, хранящих данные, выйдет из строя. Скорость записи у такого массива ниже, чем у нулевого рейда, но скорость чтения остается такой же. Для дополнительной безопасности можно использовать резервный spare диск (запасной). Он нужен для копирования данных с винчестеров из массива в случае критической ситуации.  

Преимущества массива Raid 5 состоят в том, что:  
нет необходимости покупать огромное число жестких дисков для обеспечения производительности  
можно восстановить потерянные данные с отказавших дисков  
такая конфигурация идеальна для хранилищ данных  

Что такое Raid 10  
Массив под номером 10 является симбиозом 0 и 1. Одна из самых надежных конфигураций массивов. Такой рейд содержит четное число жестких дисков для создания зеркал жестких дисков и суммирования общего объема. Самый эффективный в плане производительности и безопасности массив, недостатком которого можно назвать высокую стоимость сбора. Как правило, он используется для хранения данных в серверах баз данных.  
аппаратный, софтфовый и fake raid что это?  
Программный RAID — наименее затратный вариант, но и наименее производительный. Массив создается средствами операционной системы, вся нагрузка по обработке данных «ложится на плечи» центрального процессора.  
Fake-RAID — микрочип, установленный на материнскую плату, который берет на себя часть функционала аппаратного RAID-контроллера, работая в паре с центральным процессором. Этот подход работает чуть быстрее, чем программный RAID, но надежность у такого массива оставляет желать лучшего.  
Аппаратный RAID — это отдельный контроллер с собственным процессором и кэширующей памятью, полностью забирающий на себя выполнение всех дисковых операций. Наиболее затратный, однако, самый производительный и надежный вариант для использования.  
Что такое LVM? Для чего применяется?  
LVM — это дополнительный слой абстракции от железа, позволяющий собрать кучи разнородных дисков в один, и затем снова разбить этот один именно так как нам хочется  
Опишите структуру LVM  
1. PV (Physical Volume) — физические тома (это могут быть разделы или целые «неразбитые» диски)  
2. VG (Volume Group) — группа томов (объединяем физические тома (PV) в группу, создаём единый диск, который будем дальше разбивать так, как нам хочется)  
3. LV (Logical Volume) — логические разделы, собственно раздел нашего нового «единого диска» ака Группы Томов, который мы потом форматируем и используем как обычный раздел, обычного жёсткого диска.  


Лабораторная:  
Добавить в виртуальном сервере два hdd  
Собрать на них raid1 массив  

mdadm --create --verbose /dev/md0 --level=1
--raid-devices=2 /dev/sdb1 /dev/sdc1  
![image](https://user-images.githubusercontent.com/70812795/116358184-cacb4c80-a816-11eb-8f4b-a4de73e4d60c.png)  
![image](https://user-images.githubusercontent.com/70812795/116405066-adaf7180-a848-11eb-9619-4a05dcf0b623.png)  
поверх raid массива развернуть lvm  
![image](https://user-images.githubusercontent.com/70812795/116405766-6f668200-a849-11eb-9410-aad27fc3e37c.png)  
![image](https://user-images.githubusercontent.com/70812795/116407401-2dd6d680-a84b-11eb-93ee-bd76b840d202.png)  
создать файловую систему в lvm разделах и примонтировать в систему  
![image](https://user-images.githubusercontent.com/70812795/116413373-fd923680-a850-11eb-8e46-17df7e198599.png)  
продемонстрировать умение замены жесткого диска  
![image](https://user-images.githubusercontent.com/70812795/116414043-94f78980-a851-11eb-861d-2d889f677246.png)  
![image](https://user-images.githubusercontent.com/70812795/116414293-c5d7be80-a851-11eb-8a89-25e58dea95dd.png)  
![image](https://user-images.githubusercontent.com/70812795/116414320-cbcd9f80-a851-11eb-842c-90791aab8093.png)  

расширить размер раздела за счет неиспользуемого пространтсва в raid массиве  
mdadm --manage /dev/md0 --fail /dev/sdb mdadm --manage /dev/md0 --remove /dev/sdb sfdisk -d /dev/sdc | sfdisk /dev/sdb  
![image](https://user-images.githubusercontent.com/70812795/116414427-e30c8d00-a851-11eb-9ee6-1dd23ce37e63.png)
