link: https://docs.openwebui.com/#open-webui-bundled-with-ollama

This is the manual install of Open WebUI

This program and scripts need python 3.11 

Open WebUI needs a virtual environment for Python
   They suggest uv .. you could use conda.
   for some reason it is NOT creating a venv using uv in the normal way.  
   See the data directory

Currently my ollama is installed in native Windows .. not wsl
If Open WebUI is installed as a docker container under wsl i
.. it will not see my already downloaded models.

Installing Open WebUI manually on native Windows i
.. allows it to see my already downloaded models! 
.. allows the hope for a new ollama that supports my gpu

These are Windows installation notes.
Mac and Linux are simular.  One would have to make a new install-uv program and new run-open-webui scripts.

1. Install the uv .. see the install-uv.ps1 -- you could use conda. The both support MacOS, Windows, Linux.
   This will allow the use of older python executibles and older python models.
   ONLY in this instance.

2. Run the web server run-open-webui.ps1 
   a. The first execution it will ask for log in info
   b. It WILL find your existing ollama files.
   c. I am installing the full version which has PostgreSQL code.
      There is a comment for the lighter verson.
   d. I have not linked the Database yet which I suspect is for RAG
   e. This service must be manually started for now -- development.

 3. Browse to the link below and follow the prompts.
    http://localhost:8080/
 
 4. Near the top left there is a Ollama Model dropdown selector.  -- like ChatGPT
    This is where the previously downloaded Ollama models are listed
    

