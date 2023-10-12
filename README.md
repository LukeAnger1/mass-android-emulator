# This has only been tested with ubuntu. If you have a mac the install is a different package

# run the install with the bellow command ONLY IF you have ubuntu
sudo ./install.sh
# if you don't have ubuntu, run the same commands but switch the cmdline-tools package with your version

# put the contents of the cmdline-tools into a new folder in the same directory called latest

# make the ANDROID_SDK_ROOT in the ~/.bashrc file
export ANDROID_SDK_ROOT=<path to the unzipped file from ./install.sh>

# install the needed sdk packages through sdkmanager in the cmdline-tools/bin folder
./sdkmanager --install "platform-tools"
./sdkmanager --install "emulator"

# To install a device
	# go to the cmdline-tools/bin folder and run this command to get the image
		./sdkmanager --install "system-images;android-34;google_apis;x86_64"
	# run this command to get platform stuff
		./sdkmanager --install "platforms;android-34"
	# run this command to add the AVD (the new virtual device!)
		./avdmanager create avd --name "MyPixelAVD" --device "pixel_3a" --package "system-images;android-34;google_apis;x86_64"
	# navigate out of this directory and into the emulator directory and run this command to start the emulator
		./emulator -avd MyPixelAVD
		

# TODO: expand on this, but mostly ignore unless need
# These are helpful commands
In the command-line tools bin folder there is an sdkmanager and avdmanager
	Run them like this ./sdkmanager and ./avdmanager in the bin folder from the terminal

# To install a new image file, for example
./sdkmanager "system-images;android-30;default;x86_64"

# TODO: This doesn't work as a platform is needed
# To create a new virtual device, for example
./avdmanager create avd -n test -k "system-images;android-30;default;x86_64"

# in platform-tools this will record device input
./adb -s 'emulator-5554' shell getevent -t > input_events.txt
# TODO: convert the file to actually be able to run
./adb -s 'emulator-5554' shell < input_script.txt
