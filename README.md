# This has only been tested with WSL and ubuntu. If you have a mac the install is a different package, but hopefully the sdkmanager, avdmanager, and ... are the same

# run the install with the bellow command
sudo ./install.sh

# put the contents of the cmdline-tools into a new folder in the same directory called latest

# make the ANDROID_SDK_ROOT in the ~/.bashrc file
export ANDROID_SDK_ROOT=<path to the unzipped file from ./install.sh>

# install the needed sdk packages through sdkmanager in the cmdline-tools/bin folder
./sdkmanager --install "platform-tools"
./sdkmanager --install "emulator"



# TODO: expand on this
# These are helpful commands
In the command-line tools bin folder there is an sdkmanager and avdmanager
	Run them like this ./sdkmanager and ./avdmanager in the bin folder from the terminal

# To install a new image file, for example
./sdkmanager "system-images;android-30;default;x86_64"

# TODO: This doesn't work as a platform is needed
# To create a new virtual device, for example
./avdmanager create avd -n test -k "system-images;android-30;default;x86_64"

# in platform-tools this will record device input
./adb shell getevent -t > input_events.txt
