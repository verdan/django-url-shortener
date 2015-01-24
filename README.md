Django URL Shortener
====================

Customised Django URL Shortener. It uses a list of predefined words related to the actual url instead of random alpha-numeric word.

URL Shortening Scheme
---------------------

It is common for URL shortening services to create a unique key consisting of the characters a-z, A-Z, 0-9, so that a
key could be a74Bd and the corresponding shortened URL would then be http://myurlshortener.com/a74Bd.
We will not follow this scheme, but instead make use of a word list (you should have gotten a file called words.txt).
The key we use will always be a word from this word list.

Wordlist
--------

You must clean the wordlist yourself by converting all words to lowercase, and remove any characters that are
not [0-9a-z]. Create a shell command that cleans the wordlist and loads it into the database.
When a new request to shorten a URL comes from the form on the front page, the application should make a key by
trying to pick a word from the wordlist that exists in the URL.
The algorithm that picks a word from the wordlist should be fast and not take several seconds.
For example, if a user enters the URL http://techcrunch.com/2012/12/28/pinterest-lawsuit/ it should pick the first word
in the wordlist that is a part of this URL. I haven’t checked myself, but I would guess that the word in this case
would be “lawsuit”. If none of the words in the wordlist is a part of the URL, or if all words in the wordlist that
are part of the URL are already used for shortening other URLs, any word from the wordlist should be used. When all the words in the
wordlist have been used up as keys, the oldest existing key/URL should be deleted and that key should be reused for new URL submissions.

Example
I enter the URL http://techcrunch.com/2012/12/28/pinterest-lawsuit/ into the field on the frontpage and press enter.
The shortened URL I get back on the result page would then be http://myurlshortener.com/lawsuit/ if lawsuit is the first word
in the wordlist that is part of the URL and that is not already used for any other shortened URL.
If I would then go to the front page again and enter the URL http://lawsuit.se the shortened URL could be
http://myurlshortener.com/windmill/, as no unused word in the wordlist was part of the URL and the application picked a random word from the wordlist.

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
            
Future Plans
------------

Added IP address field in the Tiny URL model to keep track of the users and other reports related stuff.
Created Generic Models Manager.
Base presenter for future implementations of content renderings.
            
            