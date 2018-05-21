# Makefile for: \
	Automated execution of code upon change. \
	Faster pushing changes to repo. \

# Requires inotifywait, part of inotify-tools (Debian/Ubuntu: apt-get install inotify-tools)

# Written by Jennie Zheng. Modified by Haoyu Yun. \
# Modified: 2017 Sep 23

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
	# g++ $(script); ./a.out;
	python3 $(script);

push:
	git add .
	echo -n "Message: "
	read msg; \
	echo "git commit -am" $$msg; \
	git commit -am "$$msg";
	git push origin master
