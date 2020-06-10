# Makefile for: \
	Automated execution of code upon change. \
	Faster pushing changes to repo. \

# Requires inotifywait, part of inotify-tools (Debian/Ubuntu: apt-get install inotify-tools)

# Written by Jennie Zheng and Haoyu Yun. \
# Modified: 2020 Jun 10

# Example: make script="tmp/A.py"
default:
	make run;
	@#make watch --silent;

watch:
	while true; do \
		make run ; \
		#wait for changes to script \
		inotifywait -qe modify $(script) >> /dev/null; \
	done

run: $(script)
	python3 $(script);
	@# ifeq ($(findstring cpp, $(script)),)
	@# 	g++ -std=c++11 $(script) -o ./A.out; ./A.out;
	@# endif
	@# ifeq ($(findstring py, $(script)),)
	@# 	autopep8 $(script) --select=E1 --in-place;	# to fix indentation
	@# 	python3 $(script);
	@# endif

push:
	git add .
	echo -n "Message: "
	read msg; \
	echo "git commit -am" $$msg; \
	git commit -am "$$msg";
	#git push origin master
