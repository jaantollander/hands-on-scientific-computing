all:
		python source/wordcount.py data/abyss.txt processed_data/abyss.dat
		python source/wordcount.py data/isles.txt processed_data/isles.dat
		python source/wordcount.py data/last.txt processed_data/last.dat
		python source/wordcount.py data/sierra.txt processed_data/sierra.dat
		python source/plotcount.py processed_data/abyss.dat results/abyss.png
		python source/plotcount.py processed_data/isles.dat results/isles.png
		python source/plotcount.py processed_data/last.dat results/last.png
		python source/plotcount.py processed_data/sierra.dat results/sierra.png
		python source/zipf_test.py processed_data/abyss.dat processed_data/isles.dat processed_data/last.dat processed_data/sierra.dat > results/results.txt

clean:
		rm -rf processed_data/* results/*

.PHONY:
		all clean
