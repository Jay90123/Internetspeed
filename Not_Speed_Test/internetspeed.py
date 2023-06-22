import math
import speedtest

wifi = speedtest.Speedtest()

print("getting download speed")
download_speed = wifi.download()

print("Getting upload speed")
upload_speed = wifi.upload()

download = int(download_speed/1000000)
upload = int(upload_speed/1000000)

print("Download Speed:", download, "Mbps")
print("Upload speed:", upload,"Mbps")