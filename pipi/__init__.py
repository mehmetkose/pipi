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
    packages = sys.argv[1:]
    for package in packages:
        if not package_slug(package) in installed_package_slugs:
            install_command = "pip install %s" % (package)
            process = subprocess.Popen(install_command.split(), stdout=subprocess.PIPE)
            result = False
            for line in process.stdout.readlines():
                line = str(line)
                if "Successfully installed" in line:
                    for piece in line.split():
                        if len(piece)>0 and package in piece:
                            correct_version = piece.split('-')[-1]
                            requirement_line = "%s==%s\n" % (package,
                                                                correct_version)
                            write_to_file(requirement_line,requirements_path)
                            result = "pipi: %s installed & saved." % \
                                  requirement_line.strip()
                elif "already satisfied: %s" % (package) in line:
                    result = "pipi: %s is already installed" % package
                    requirement_line = "%s\n" % (package)
                    write_to_file(requirement_line, requirements_path)
                elif "BrokenPipeError" in line:
                    break
                else:
                    #print(str(line))
                    print(str(line))
                    #print(type(str(line)))
            print("\n"+result)
        else:
            print("pipi: %s is already installed" % package)


if __name__ == "__main__":
    main()
