import requests
import tikvid

video = input("URL: ")
id = tikvid.parseLink(video)

output = tikvid.downloadLink(id)
v_content = requests.get(output)

with open("video.mp4", "wb") as f:
	f.write(v_content.content)

print("Video downloaded!")