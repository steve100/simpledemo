mkdir c:\sqlite3

copy sqlite*.zip c:\sqlite3

cd c:\sqlite3
unzip -t *.zip


unzip sqlite-dll-win-x64-3510000.zip
unzip sqlite-doc-3510000.zip
unzip  sqlite-tools-win-x64-3510000.zip

rem add c:\sqlite3 to the system environment variable path
rem either use the gui or run below run as administrator
rem 
rem ./newsqlite3path.ps1

