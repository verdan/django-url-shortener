Django URL Shortener
====================

Customised Django URL Shortener. It uses a list of predefined words related to the actual url instead of random alpha-numeric word.

Getting Started
---------------

I'm assuming you have Python installed. It is preferable to have a virtual environment for the project libraries.
Also assuming you've git setup on your system.

Setting Up the Virtual Environment (skip this if you want to mess-up your python libraries :P)
-------------------------------------------------------------------------------------------

If you're using pip to install packages (and I can't see why you wouldn't), you can get both virtualenv and virtualenvwrapper by simply installing the latter.

            pip install virtualenvwrapper

After it's installed, add the following lines to your shell's start-up file (.zshrc, .bashrc, .profile, etc).

            export WORKON_HOME=$HOME/.virtualenvs
            export PROJECT_HOME=$HOME/directory-you-do-development-in
            source /usr/local/bin/virtualenvwrapper.sh

Reload your start up file (e.g. source .bashrc) and you're ready to go.

Creating a virtual environment is simple. Just type

            mkvirtualenv short

or If already created the Virtual Environment, just start the environment by typing

            workon short


Getting the App Running
-----------------------

Installing Python Packages and getting the app running is just like eating chocolate.

            cd /path/where/you/want/your/project
            git clone git@bitbucket.org:verdanmahmood/django-url-shortener.git
            cd django-url-shortener/
            
Packages will be installed with a shell command **install-dev**
This command installs the packages in the requirement file, runs the syncdb and migrate commands itself.
            
            ./url_shortner.sh install-dev
            
Start the Server
            
            python manage.py runserver
            
### Having Permissions Errors Running Shell Commands ? Try this: 
            cd /path/to/project
            chmod u+rwx url_shortner.sh
            
            
Loading the Words Database
--------------------------
            
Secret words are placed in the file in fixtures directory in the repository.
You can load the words in the database by two ways.

from custom management command:

            python manage.py upload_words
            
or, by using a shell command.
            
            ./url_shortner.sh load-words
            
Running the Tests
-----------------
            
Tests can also be run using shell command:

            ./url_shortner.sh tests
            
            