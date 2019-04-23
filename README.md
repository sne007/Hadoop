# Hadoop

# To clone:

git clone https://github.com/sne007/Hadoop.git

# To get data:
hadoop fs -get /user/tatavag/nyc.data /home/nyc
hadoop fs -get /user/tatavag/nyc.data ~/Hadoop/nyc.csv

hadoop fs -put nyc.csv /user/challasy/nyc.csv (This Exists)

# Map Reduce Command:

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/challasy/mapper.py -mapper /home/challasy/mapper.py -file /home/challasy/reducer.py -reducer /home/challasy/reducer.py -input /user/challasy/nyc.csv -output /user/challasy/mysummary

# To give persmissions:

chmod +x mapper.py && chmod +x reducer.py

# To Execute:

(outputname can be replaced with any other name)

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/mapper.py -mapper ~/mapper.py -file ~/reducer.py -reducer ~/reducer.py -input /user/challasy/nyc.csv -output /user/challasy/outputname

# Downloading file from hdfs to local machine:

hadoop fs -get /user/challasy/outputname/part-00000 ~/outputname.txt

# To See the output:

hadoop fs -cat /user/challasy/outputname/*
