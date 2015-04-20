# scratch_extensions
HTTP Extensions for MIT Scratch 2.0

usage:
- install prerequisites (virtualenv lib already provided in this repository)
- start python script (for instance scratch_meteo.py)
- browse to http://localhost:4000 and click on the first link to download the .s2e file
- keep the script running
- start Scratch 2.0 offline editor
- shift-click on the "File" menu, select "import HTTP extension" 
- give the path to the file just downloaded
- you should have some new "blocks" defined

how does it work ?

The best explanation is here:
http://wiki.scratch.mit.edu/wiki/Scratch_Extension#HTTP_Extensions

a python module called [blockext](https://github.com/blockext) provides an easy to use interface for new block definitions. Adapted to run with python3.4

Tested only on Linux and Windows.




 

