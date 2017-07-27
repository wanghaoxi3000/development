# test_leds.sh

for i in $(seq 10);
do
	n=$i
	echo $n
	echo $n > temp

	n=$(rev temp)
	echo $n > /dev/s3c6410_leds

	sleep 1
done;
