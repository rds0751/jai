#!/bin/bash
ls /home/Bubbas
pip3 install -r /home/Bubbas/requirements.txt
python3 /home/Bubbas/manage.py migrate
python3 /home/Bubbas/manage.py runserver