echo "starting the installation"

echo "updating system and installing dependencies through apt"
apt update
apt upgrade -y
apt install openjdk-17-jdk wget unzip -y

echo "getting the main package"
wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
unzip commandlinetools-linux-10406996_latest.zip

