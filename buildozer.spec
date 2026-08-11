[app]

# (str) Title of your application
title = Arh AI App

# (str) Package name
package.name = arhiapp

# (str) Package domain (needed for android packaging)
package.domain = org.arh

# (str) Source files to include (let it find everything in the current directory)
source.dir = .

# (list) Source files to include (let it include common extensions)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Android SDK version to use
android.sdk = 33

# (str) Supported orientations
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

# (str) 
osx.python_version = 3

# (str) Kivy version to use
osx.kivy_version = 1.9.1

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
