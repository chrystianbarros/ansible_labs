import subprocess
import logging
import sys

# Updates the system packages to ensure consistency
def update_apt_packages(log_directory):
	print('--- TASK: Updating apt packages ---')
	# Configure logging
	logfile_path = f"{log_directory}/update_apt_packages.log"
	logging.basicConfig(
		filename=logfile_path,
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s'
	)

	command = ["sudo", "apt", "update"]
	try:
		result = subprocess.run(command, capture_output=True, text=True, check=True)
		logging.info("--- Command Standard Output ---")
		if result.stdout:
			logging.info(result.stdout)
		
		logging.info("--- Command Standard Error ---")
		if result.stderr:
			logging.info(result.stderr)

		print(f"pip installation was successful. Details are in {logfile_path}")
	except subprocess.CalledProcessError as e:
		logging.error("--- Command Failed ---")
		logging.error(f"Command: {e.cmd}")
		logging.error(f"Return Code: {e.returncode}")
		logging.error(f"Standard Output:\n{e.stdout}")
		logging.error(f"Standard Error:\n{e.stderr}")
		
		print(f"Updating apt packages failed. Check {logfile_path} for details.", file=sys.stderr)

# Install the pip package
def install_pip(log_directory):
	print('--- TASK: Installing python3-pip using apt ---')
	# Configure logging
	logfile_path = f"{log_directory}/install_pip.log"
	logging.basicConfig(
		filename=logfile_path,
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s'
	)

	command = ["sudo", "apt", "install", "-y", "python3-pip"]
	try:
		result = subprocess.run(command, capture_output=True, text=True, check=True)
		logging.info("--- Command Standard Output ---")
		if result.stdout:
			logging.info(result.stdout)
		
		logging.info("--- Command Standard Error ---")
		if result.stderr:
			logging.info(result.stderr)

		print(f"pip installation was successful. Details are in {logfile_path}")
	except subprocess.CalledProcessError as e:
		logging.error("--- Command Failed ---")
		logging.error(f"Command: {e.cmd}")
		logging.error(f"Return Code: {e.returncode}")
		logging.error(f"Standard Output:\n{e.stdout}")
		logging.error(f"Standard Error:\n{e.stderr}")
		
		print(f"pip installation failed. Check {logfile_path} for details.", file=sys.stderr)
	except FileNotFoundError:
		print("Error: 'sudo' or 'apt' command not found. Ensure they are in your PATH.")

# Install the Ansible pip package in determined version
def install_ansible_pip_package(log_directory, version):
	print(f'--- TASK: Installing ansible-core:{version} using pip ---')
	command = [sys.executable, "-m", "pip", "install", f"ansible-core=={version}", "--break-system-packages"]
	# Configure logging
	logfile_path = f"{log_directory}/install_ansible_pip_package.log"
	logging.basicConfig(
		filename=logfile_path,
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s'
	)

	try:
		result = subprocess.run(command, capture_output=True, text=True, check=True)
		logging.info("--- Command Standard Output ---")
		if result.stdout:
			logging.info(result.stdout)
		
		logging.info("--- Command Standard Error ---")
		if result.stderr:
			logging.info(result.stderr)
			
		print(f"Ansible pip packages installation was successful. Details are in {logfile_path}")
	except subprocess.CalledProcessError as e:
		logging.error("--- Command Failed ---")
		logging.error(f"Command: {e.cmd}")
		logging.error(f"Return Code: {e.returncode}")
		logging.error(f"Standard Output:\n{e.stdout}")
		logging.error(f"Standard Error:\n{e.stderr}")
		
		print(f"Ansible pip packages installation failed. Check {logfile_path} for details.", file=sys.stderr)
	except FileNotFoundError:
		# This block is for cases where the command itself is not found.
		logging.error("The 'sudo' or 'pip' command was not found.")
		print("Error: Required command not found. Please ensure 'sudo' and 'pip' are installed and in your PATH.", file=sys.stderr)

# Install ansible-core using apt installer
def install_ansible_core(log_directory):
	print('--- TASK: Installing ansible-core using apt ---')
	# Configure logging
	logfile_path = f"{log_directory}/install_ansible_core.log"
	logging.basicConfig(
		filename=logfile_path,
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s'
	)

	command = ["sudo", "apt", "install", "-y", "ansible-core"]
	try:
		result = subprocess.run(command, capture_output=True, text=True, check=True)
		logging.info("--- Command Standard Output ---")
		if result.stdout:
			logging.info(result.stdout)
		
		logging.info("--- Command Standard Error ---")
		if result.stderr:
			logging.info(result.stderr)
			
		print(f"Ansible-core installation was successful. Details are in {logfile_path}")
	except subprocess.CalledProcessError as e:
		logging.error("--- Command Failed ---")
		logging.error(f"Command: {e.cmd}")
		logging.error(f"Return Code: {e.returncode}")
		logging.error(f"Standard Output:\n{e.stdout}")
		logging.error(f"Standard Error:\n{e.stderr}")
		
		print(f"Ansible-core installation failed. Check {logfile_path} for details.", file=sys.stderr)
	except FileNotFoundError:
		# This block is for cases where the command itself is not found.
		logging.error("The 'sudo' or 'apt' command was not found.")
		print("Error: Required command not found. Please ensure 'sudo' and 'apt' are installed and in your PATH.", file=sys.stderr)
	except Exception as e:
		# Catch any other unexpected exceptions.
		logging.critical(f"An unexpected error occurred: {e}")
		print(f"An unexpected error occurred during installation. Check {logfile_path}.", file=sys.stderr)