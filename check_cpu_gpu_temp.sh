# I am using this on my Raspberry Pi 4 B to check the temps of my GPU/CPU
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "------------------------------------"
echo "GPU => $(/usr/bin/vcgencmd measure_temp)"     #adjust path if vcgencmd not found - ($ which vcgencmd) in terminal
echo "CPU => $((cpu/1000))'C"

# chmod +x check_cpu_gpu_temp.sh        to make it executable
# ./check_cpu_gpu_temp.sh               to run