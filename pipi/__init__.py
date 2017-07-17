#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, subprocess, os

def package_slug(package_name):
    return package_name.split('==')[0].strip()

def run_command(command):
    try:
        return subprocess.check_output(command.split())
    except:
        pass
    return False

def write_to_file(line, file_path):
    with open(file_path, "a") as myfile:
        myfile.write(line)

def main():
    # get path
    current_dir = os.getcwd()
    # check requirements.txt
    requirements_path = "%s/requirements.txt" % (current_dir)
    if not os.path.isfile(requirements_path):
        with open(requirements_path, 'a'):
            os.utime(requirements_path, None)
    # read lines
    data = open(requirements_path, 'r')
    installed_packages = [line.strip("\n") for line in data.readlines()]
    installed_package_slugs = [package_slug(package) for package in installed_packages]
    # get arguments
    packages_to_install = sys.argv[1:]
    for package_to_install in packages_to_install:
        if not package_slug(package_to_install) in installed_package_slugs:
            install_command = "pip install %s" % package_to_install
            result = run_command(install_command)
            if result:
                for line in result.lower().split("\n"):
                    if "successfully installed" in line:
                        for piece in line.split():
                            if package_to_install in piece:
                                correct_version = piece.split('-')[-1]
                                requirement_line = "%s==%s\n" % (package_to_install,
                                                                 correct_version)
                                write_to_file(requirement_line,requirements_path)
                                print("pipi: %s installed & saved to requirements.txt" % \
                                      requirement_line.replace("\n",""))
            else:
                print("pipi: %s could not be installed properly" % package_to_install)
        else:
            print("pipi: %s is already installed" % package_to_install)


if __name__ == "__main__":
    main()
