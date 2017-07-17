#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, subprocess, os

def package_slug(package_name):
    return package_name.split('==')[0].strip()

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
            install_command = "pip install %s" % (package_to_install)
            process = subprocess.Popen(install_command.split(), stdout=subprocess.PIPE)
            for line in process.stdout.readlines():
                if "Successfully installed" in line:
                    for piece in line.split():
                        if package_to_install in piece:
                            correct_version = piece.split('-')[-1]
                            requirement_line = "%s==%s\n" % (package_to_install,
                                                                correct_version)
                            write_to_file(requirement_line,requirements_path)
                            print("pipi: %s installed & saved." % \
                                  requirement_line.replace("\n",""))
                elif "already satisfied: %s" % (package_to_install) in line:
                    print("pipi: %s is already installed" % package_to_install)
                    requirement_line = "%s\n" % (package_to_install)
                    write_to_file(requirement_line,requirements_path)

        else:
            print("pipi: %s is already installed" % package_to_install)

if __name__ == "__main__":
    main()
