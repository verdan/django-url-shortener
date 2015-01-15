#!/bin/bash

function heading {
	TEXT="$1" && [[ -z $1 ]]  && TEXT="####"
	echo "##########################$TEXT##############################"
}


function install-dev {
	heading "##########################"
	heading " Installing dev environment "
	heading " (it may take some time...) "

	DJANGO_SETTINGS_MODULE=urlshortener.settings pip install -r requirements.txt

     python manage.py syncdb --noinput
     python manage.py migrate
}

function load-words {
	DJANGO_SETTINGS_MODULE=urlshortener.settings
     python manage.py upload_words
}


function run-tests {
	DJANGO_SETTINGS_MODULE=urlshortener.settings
     python manage.py test
}

case $1 in

install-dev )
    install-dev
    heading "~~~~~~~~~installed~~~~~~~~~~"
	;;

load-words )
    load-words
	;;

tests )
    run-tests
	;;

* )
	help
	;;

esac