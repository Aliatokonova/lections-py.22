Git - это расспределенная  система контроля версии
имеет два место для хранения  локальная и репразиторий это система для отслеживания и ведение историии изменений ваших историй 
Репозиторий - хранилище ваших файлов которые вы отлеживаете при помощи гита и их изменения.

 Команды git - нужен для того чтобы создать новый репозиторий на локальном пк ,создает она в той директории где вы запускаете эту команду .
 git add -  когда мы созаем и изменяем файлы  то припомощи этой команды мы загружаем все изменения в промежуточное место хранения 
  git add < file_name>
  git add . -> все в текущей директории 
  
  git commit - как только мы настигаем определенного момента в разработке то мы тогда сохраняем и коментируем все наши изменения в репозитории тоесть это команда нашей фиксации изменений в репо . )
  git commit -m ' <comment>' - 
  .hello 
  
  
  
 git remote add -это команда для того чтобы связатьваш локальный репозиторий  с удаленным репозиторием(репо в гитхабе)
  git remote add <название нашего подключения> < ссылка на репозиторий>
  git remote add origin <url> 
   git push -после комита измененний при помощи этой команды мы отправляем наши изменения в файлах на удаленный репозиторий
      git push <origin> <название ветки (main)>
   git push origin main - 
.

----------------------------------------------------------------------------------------------
1git init
git branch -M main (переименовываем главную ветку с master на main
git add .
git commit -m 'comment' (все добавленно в локальный peпо)
 git remote add origin <url>
 git push origin main
 //////////////// когда только создаем репозиторий
 
 ----------------------------------------------------------------------------------------------
 git add .
 git commit -m 'comment'
 git push origin main
