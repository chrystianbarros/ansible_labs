import argparse
from modules import install_packages

parser = argparse.ArgumentParser(
	prog='Setup Ansible',
	description='Program to setup Ansible and its dependencies',
	epilog='For more information, read the "README.md" file in the ansible_installtation directory')

parser.add_argument('--ansible_version', required=True, type=str, help='Ansible version to be installed')
parser.add_argument('--log_directory', required=True, type=str, help='Directory for storing log files')
args = parser.parse_args()

# Updates system packages
install_packages.update_apt_packages(args.log_directory)

# Ensures pip is installed
install_packages.install_pip(args.log_directory)

# Ensures Ansible pip package is present
install_packages.install_ansible_pip_package(args.log_directory, args.ansible_version)

# Ensures pip packages are installed
install_packages.install_ansible_core(args.log_directory)