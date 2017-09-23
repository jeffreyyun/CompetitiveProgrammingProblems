# Written by Jennie Zheng. Modified by Haoyu Yun. \

# Makefile for: \
	Automated execution of code upon change. \
	Faster pushing changes to repo. \

# Example: make script="a.py"
default:
	make run;
	make watch --silent;

watch:
	while true; do \
		make run ; \
		#wait for changes to script \
		inotifywait -qe modify $(script) >> /dev/null; \
	done

run:
	#if running c++, then gcc compile and then run
	python3 $(script);

push:
	git add .
	echo -n "Message: "
	read msg; \
	echo "git commit -am" $$msg; \
	git commit -am "$$msg";
	git push origin master
