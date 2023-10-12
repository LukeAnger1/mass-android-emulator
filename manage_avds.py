import subprocess
import config
import re
import platform

def list_known_devices():
    try:
        # Execute the avdmanager command to list known devices
        result = subprocess.run([config.avdmanager, 'list', 'avd'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # print("Known devices:")
            # print(result.stdout)
            return result.stdout
        else:
            print("Error listing known devices:")
            print(result.stderr)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_virtual_device(name = None, device = "pixel_3a", package = "system-images;android-34;google_apis;x86_64"):

    # this will create the next device in the list 
    if name == None:
        # this takes the output from list_known_devices and finds its length to find the number for the next device. Then converts it to a str
        name = str(len(re.findall(r'Name:\s+(.+)', list_known_devices())))

    try:
        # Execute the avdmanager command to create a new virtual device
        command = [
            config.avdmanager,
            'create',
            'avd',
            '--name', name,
            '--device', device,
            '--package', package
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f"Virtual device '{name}' created successfully.")
        else:
            print(f"Error creating virtual device '{name}':")
            print(result.stderr)
            print('if device name is number, retrying with a higher number')
            if name.isdigit():
                print('running again with one higher name')
                create_virtual_device(name = str(int(name) + 1))
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def remove_virtual_device(avd_name):
    try:
        # Execute the avdmanager command to delete the specified AVD
        command = [
            config.avdmanager,
            'delete',
            'avd',
            '--name', avd_name
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f"AVD '{avd_name}' removed successfully.")
        else:
            print(f"Error removing AVD '{avd_name}':")
            print(result.stderr)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def start_emulator(avd_name, headless = False):
    # TODO: this might actually be id
    # TODO also has to run in parallel to get the apk install to work
    # TODO: add a headless emulator option
    try:
        # TODO: this is untested for windows
        if platform.system() == 'Windows':
            # TODO: this is using a different file, keep as this but may need to switch to use the config later
            emulator_command = 'emulator.exe'
        else:
            emulator_command = config.emulator

        # Replace 'avd_name' with the name of the AVD you want to start
        emulator_command = f'{emulator_command} -avd {avd_name}'

        # this will add the window if needed, mainly for testing
        if headless:
            emulator_command += ' -no-window'

        # Run the emulator command using subprocess
        process = subprocess.Popen(emulator_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        if process.returncode == 0:
            print(f'Emulator {avd_name} started successfully')
        else:
            print(f'Failed to start emulator {avd_name}')
            print(f'Error message: {err.decode("utf-8")}')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

def install_apk(avd_name, apk_path, started = False):
    # this is the case when the emulator hasnt been started yet
    if not started:
        # TODO: get this line to run in parallel, the apk wont install until this is closed defeating the purpose
        start_emulator(avd_name, headless=True)

    try:
        # Use adb to install the APK on the specified AVD by name
        adb_install_command = [config.adb, '-s', f'emulator-{avd_name}', 'install', '-r', apk_path]
        result = subprocess.run(adb_install_command, capture_output=True, text=True)
        
        # Check if the installation was successful
        if "Success" in result.stdout:
            print(f"APK '{apk_path}' installed successfully on '{avd_name}'.")
        else:
            print(f"Error installing APK '{apk_path}' on '{avd_name}':")
            print(result.stderr)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    # Example usage
    list_known_devices()
    print(list_known_devices())
    print('made it here 2')
    start_emulator('3', headless=True)
    print(f'made it here')