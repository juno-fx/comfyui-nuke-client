.PHONY: venv requirements

requirements:
	mkdir -p requirements
	python3.7 -m venv venv
	venv/bin/pip install -r requirements.txt -t requirements/

nuke:
	NUKE_DISABLE_FRAMESERVER=1 NUKE_PATH=$(shell pwd) /opt/Nuke14.0v5/Nuke14.0 -nc