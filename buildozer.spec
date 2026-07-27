[app]

# (str) Title of your application
title = My App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp

# (str) Source code where the main.py live
source.dir = my_kivy_app

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*, images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directory names to not include at all
# source.exclude_dirs = tests, bin, .git

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license, images/*/.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# requirements = python3,kivy
requirements = python3,kivy==2.3.0

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OS X Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android Specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (bool) Accept Android NDK license
android.accept_ndk_license = True

# (list) Android AAR archives to add (let empty to not add any)
# android.add_aars =

# (list) Gradle dependencies to add (let empty to not add any)
# android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Activity class to override
# android.entrypoint = org.kivy.android.PythonActivity

# (list) Android additional Java code to include
# android.add_src =

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
# p4a.source_dir =

# (str) python-for-android fork to use, defaults to kivy
# p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) python-for-android specific revision to use, defaults to HEAD
# p4a.revision = HEAD

# (str) Android SDK directory (if empty, it will be automatically downloaded)
# android.sdk_path =

# (str) Android NDK directory (if empty, it will be automatically downloaded)
# android.ndk_path =

# (str) Android ANT directory (if empty, it will be automatically downloaded)
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = True

#
# iOS Specific
#

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s
