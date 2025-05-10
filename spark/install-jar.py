#!/usr/bin/env python3
import sys
import subprocess

# Example usage: ./install_jar.py "org.group:artifact:version"
maven_coord = sys.argv[1]
jar_dir = sys.argv[2]

# Split it up.
group, artifact, version = maven_coord.split(":")

# Convert group to URL path (org.group -> org/group)
group_path = group.replace(".", "/")

# Now create the URL.
download_url = (
    f"https://repo1.maven.org/maven2/"
    f"{group_path}/{artifact}/{version}/"
    f"{artifact}-{version}.jar"
)

# Download to /opt/spark/jars
subprocess.run(
    [
        "wget",
        "-q",  # Quiet mode
        download_url,
        "-P",
        jar_dir,  # Save to this directory
    ],
    check=True,
)

print(f"Installed: {maven_coord}")
