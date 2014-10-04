set data=C:\Games\AdventureTime\data
set tmp=tmp
set bak=bak
set res=res

rem create backup directory (only once!) and backup original files
if not exist %bak% (
	mkdir %bak%
	copy /y %data%\global.pak %bak%
	copy /y %data%\menus.pak %bak%
)

mkdir %tmp%

paktools %bak%\global.pak %tmp%\global
paktools %bak%\menus.pak %tmp%\menus
paktools %bak%\shop.pak %tmp%\shop
paktools %bak%\tutorial.pak %tmp%\tutorial

python ltbtools.py .\%tmp%\global\global\localization.ltb --write < ru.txt

copy /y %res%\global\*.* %tmp%\global\global
copy /y %res%\menus\*.* %tmp%\menus\menus
copy /y %res%\shop\*.* %tmp%\shop\shop
copy /y %res%\tutorial\*.* %tmp%\tutorial\tutorial

paktools %tmp%\global global.pak
paktools %tmp%\menus menus.pak
paktools %tmp%\shop shop.pak
paktools %tmp%\tutorial tutorial.pak

copy /y menus.pak %data%\menus.pak
copy /y global.pak %data%\global.pak
copy /y shop.pak %data%\shop.pak
copy /y tutorial.pak %data%\tutorial.pak

::rmdir /s /q %tmp%
