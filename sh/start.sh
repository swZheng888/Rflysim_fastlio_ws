
roscore &
sleep 5
cd /home/adminpc/sensor_pkg && python3 lidar.py &

sleep 5
roslaunch mavros px4.launch fcu_url:="udp://:20101@192.168.2.228:20100" &

sleep 5
gnome-terminal --window --title="faster-lio" -e 'bash -c "roslaunch faster_lio mapping_rflysim.launch; exec bash;"'
sleep 10

