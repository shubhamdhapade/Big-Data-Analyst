echo "==================== System Info ===================="
echo "Current User		: $(whoami)"
echo "host Name			: $(hostname)"
echo "Operating System		: $(uname -o 2>/dev/null || uname -s)"
echo "Kernal Version		: $(uname -r)"
echo ""
echo "------ Disk Space Usage -----"
df -h /
echo ""
echo "-------- Memory Usgae -------"
free -h 2>/dev/null || vm_stat
echo "====================================================="
