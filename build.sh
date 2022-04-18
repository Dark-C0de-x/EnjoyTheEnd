echo ""
user=$(whoami)
if [ "$user" == "root" ]; then
   esroot=true
   echo "[+] Comenzando instalacion"
   echo ""
else
   esroot=false
   echo "[*] Se necesita root" 
   exit
fi
apt-get install python3
pip3 install plyer
pip3 install requests
pip3 install platform
apt-get install go -y
echo ""
echo "Instalacion completada satisfactoriamente, puede ejecutar gh0st.py"
