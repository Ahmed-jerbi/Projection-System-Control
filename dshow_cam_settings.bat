:: Shows the dshow camera settings dialogue
:: takes a camera name as an input argument, e.g. "dshow_cam_settings.bat LogitechAJ"
:: needs FFMPEG library: https://ffmpeg.org/

@echo off
ffmpeg -f dshow -show_video_device_dialog true -i video="%1" -hide_banner
if %ERRORLEVEL% neq 0 goto ProcessError

::If the camera name is invalid show the dshow devices list
:ProcessError
echo Listing available DirectShow devices: 
ffmpeg -list_devices true -f dshow -i dummy -hide_banner
pause
