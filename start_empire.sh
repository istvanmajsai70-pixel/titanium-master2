#!/bin/bash
echo "Titanium Birodalom Indítása..."
nohup python3 controller.py > /dev/null 2>&1 &
echo "A 130 bot elindult a háttérben 0-24-es üzemmódban."
echo "Használd a 'cat ~/titanium_empire/empire_status.log' parancsot az ellenőrzéshez."
