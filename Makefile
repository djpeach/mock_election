format:
	black --extend-exclude migrations .
data-dump:
	python manage.py dumpdata auth --format json --indent 2 > elections/fixtures/auth.json
	python manage.py dumpdata elections.Election --format json --indent 2 > elections/fixtures/elections.json
	python manage.py dumpdata elections.Race --format json --indent 2 > elections/fixtures/races.json
	python manage.py dumpdata elections.Candidate --format json --indent 2 > elections/fixtures/candidates.json
	python manage.py dumpdata elections.RunningMate --format json --indent 2 > elections/fixtures/running_mates.json
	python manage.py dumpdata elections.Voter --format json --indent 2 > elections/fixtures/voters.json
	python manage.py dumpdata elections.Vote --format json --indent 2 > elections/fixtures/votes.json
data-populate:
	python manage.py loaddata auth
	python manage.py loaddata elections
	python manage.py loaddata races
	python manage.py loaddata candidates
	python manage.py loaddata running_mates
	python manage.py loaddata voters
	python manage.py loaddata votes