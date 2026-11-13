[app]
title = Fanadinana Madagasikara
package.name = fanadinana
package.domain = mg.fanadinana
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,websocket-client,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
# Le serveur de dev est en HTTP (pas HTTPS) : autoriser le trafic clair
android.manifest.application_arguments = android:usesCleartextTraffic="true"

[buildozer]
log_level = 2
warn_on_root = 1
