from pathlib import Path
p = open("python3.desktop", "w")
filepath = str(Path(__file__).resolve().parent)+'/alfurqaan.py'
p.write(
'''[Desktop Entry]
Type=Application
Exec=python3 %s
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=Al Basair
Name=python3
Comment[en_US]= One ayah recite and listen on computer poweron everytime
Comment=One ayah recite and listen on computer poweron everytime
'''%filepath)
p.close()