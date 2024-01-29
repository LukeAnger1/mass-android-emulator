#!/bin/bash
# This installation script is intended to be run on a Linux machine.
# NOTE: needs to run with sudo privelege

echo "starting the installation"

echo "updating system and installing dependencies through apt"
apt update
apt upgrade -y
apt install unzip -y
apt install openjdk-17-jdk wget unzip -y

echo "getting the main package"
# IMPORTANT TODO: uncomment the below
# wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
# unzip commandlinetools-linux-10406996_latest.zip

# Get the current directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Append "cmdline-tools" folder to the ANDROID_SDK_ROOT
ANDROID_SDK_ROOT="$SCRIPT_DIR/cmdline-tools"

# Set ANDROID_SDK_ROOT environment variable
echo "export ANDROID_SDK_ROOT=\"$ANDROID_SDK_ROOT\"" >> ~/.bashrc
source ~/.bashrc

echo "Main installation completed"

# Navigate to the cmdline-tools/bin directory
cd "$ANDROID_SDK_ROOT/bin"

# Install the required SDK packages using sdkmanager
./sdkmanager --install "platform-tools"
./sdkmanager --install "emulator"

echo "Installing the needed tools"
