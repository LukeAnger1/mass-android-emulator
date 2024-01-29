#!/bin/bash
# This installation script is intended to be run on a Linux machine.
# NOTE: You may need to run this script with sudo privileges.

echo "Starting the installation"

echo "Updating system and installing dependencies through apt"
apt update
apt upgrade -y
apt install unzip -y
apt install openjdk-17-jdk wget unzip -y

echo "Getting the main package"
wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
unzip commandlinetools-linux-10406996_latest.zip

# Get the current directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Append "cmdline-tools" folder to the ANDROID_SDK_ROOT
ANDROID_SDK_ROOT="$SCRIPT_DIR/cmdline-tools"

# Set ANDROID_SDK_ROOT environment variable
echo "export ANDROID_SDK_ROOT=\"$ANDROID_SDK_ROOT\"" >> ~/.bashrc
source ~/.bashrc

# Navigate to the cmdline-tools directory
cd "$ANDROID_SDK_ROOT"

# Create a new directory for Android SDK (android_sdk)
SDK_DIR="$ANDROID_SDK_ROOT/../android_sdk"
mkdir -p "$SDK_DIR"

# Create a sub-directory called "latest" and move the original contents
mkdir -p "$SDK_DIR/latest"
mv ./* "$SDK_DIR/latest"

# Navigate to the newly created "latest" directory
cd "$SDK_DIR/latest"

# Now install the required SDK packages using sdkmanager
./bin/sdkmanager --install "platform-tools"
./bin/sdkmanager --install "emulator"

echo "Installation completed. Please run 'source ~/.bashrc' or start a new terminal session to apply changes."
