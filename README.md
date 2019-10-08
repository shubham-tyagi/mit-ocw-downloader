
# MIT-OCW Downloader

Download all video lectures from a MIT-OCW course with a single command.

## Features

* Intentionally detailed names, so that it will display and sort properly
    on most interfaces (e.g., MX Video, or VLC on Android devices).
  * URL and lecture name filters to download only video files.
  * Tested on Windows (Python 3.6).

## Instructions to download OCW using this

* [mit-ocw-downloader][1] basically needs a link to the course page of a MIT-OCW course
    (which of course has video lectures). The link would be something like [<http://ocw.mit.edu/cources/college/course-title/]>

  * Make a [virtual environment][4] for this project on your local machine and activate it.
  
  * Copy the ```download.py``` file to the folder where you want to download the video lectures.
  
  * Run ```python download.py ``` or ```python3 download.py``` in case you have more than one versions of python installed on your system.  
  
  * Enter the link of the course of which you need all the video lectures    

  * Voila! Download must have started by now.
  
## Contributions

   If you want to contribute to this project, feel free to fork it and send a PR :)

## Coming Up

* [mit-ocw-scrapper][1] only supports video content of the course presently
  but attempts are on to make it download entire contents (lecture slides, assignments, solutions,srt fileetc.)

## Contact  

  Shoot a mail at raj.tyagi2000@gmail.com
  
## Author

  [Shubham Tyagi][2]

## Inspiration

  [coursera-dl/coursera][3]

[1]: https://github.com/shubham-tyagi/mit-ocw-downloader
[2]: http://shubhamtyagi.me
[3]: https://github.com/coursera-dl/coursera
[4]: https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/
