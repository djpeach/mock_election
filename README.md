# mock_election

## Access server

SSH:
```bash
ssh -i mock-election.pem ubuntu@election.garrettpeach.com 
```

## Transfer files

SCP:
```bash
scp -r -i mock-election.pem {_config,elections,html-pages,Makefile,manage.py,requirements.txt} ubuntu@election.garrettpeach.com:/home/ubuntu/
```

## Manage server

Run Server:
[(Create screen, run server, detach from screen)](https://stackoverflow.com/questions/1188542/django-runserver-permanent)
```bash
screen -d -m python manage.py runserver 0.0.0.0:8000
```

Connect to screen
```bash
screen -r
```

Stop server
(after attaching to screen)
```bash
Ctrl + C
```


Detach from screen
```bash
Ctrl + A
d
```