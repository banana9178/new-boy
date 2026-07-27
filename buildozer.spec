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

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = kivy==2.3.0

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# Android Specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android build tools version to use
android.build_tools = 30.0.3

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (bool) Accept Android NDK license
android.accept_ndk_license = True

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = True
