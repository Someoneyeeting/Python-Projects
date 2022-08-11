cd /d C:\Program Files (x86)\Android\android-sdk\platform-tools
result="$(adb shell dumpsys input_method | grep -c "mScreenOn=true")"

if [ "$result" == 1 ]; then
    echo "Screen is already on."

else
    echo "Turning screen on."
    adb shell input keyevent 26
fi