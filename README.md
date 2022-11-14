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

Run Gunicorn:
```bash
gunicorn _config.wsgi -b 0.0.0.0:8000 --daemon
```

See Gunicorn Processes:
```bash
ps ax | grep gunicorn
```


Kill Gunicorn:
```bash
pkill -f gunicorn
```