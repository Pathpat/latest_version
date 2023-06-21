def moodle_version():
    import requests
    import json

    response = requests.get("https://api.github.com/repos/moodle/moodle/tags")
    data = response.json()
    tags = data[:5]
    versions = [] 
    for tag in tags:
        if tag["name"].startswith("v"):
            versions.append(tag["name"])
    latest_version = max(versions)
    print("moodle -v",latest_version)
   

moodle_version()