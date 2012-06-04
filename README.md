emoRHC
======

Creates startscript for google chrome semi-automatically. 

Dependencies
------------

- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

Installing Dependencies on Fedora Linux
---------------------------------------

    sudo yum install python-pip
    sudo pip-python install beautifulsoup4

Install
-------

    sudo ln -s `pwd`/chrome /usr/bin/chrome

Remove
------

     sudo unlink /usr/bin/chrome
     
Usage
-----

Uncomment your wanted flags from `chrome` and run it using

    chrome
    
Make sure to keep your modifications under version control

    git add chrome
    git commit chrome

When chrome changes the command line flags, update `chrome` using
    
    python Updater.py
    
and merge them with your version using an powerful merge tool like meld:

    meld . &
    
finally track your modifications

    git add chrome
    git commit
