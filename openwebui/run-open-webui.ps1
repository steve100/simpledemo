mkdir C:\open-webui\data -Force

$env:DATA_DIR="C:\open-webui\data"; 

# uvx --python 3.11 open-webui@latest serve
 uvx --python 3.11 open-webui[all]@latest serve
