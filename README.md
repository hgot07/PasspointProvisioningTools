# PasspointProvisioningTools
Tools and example codes for Passpoint profile provisioning, mainly for OpenRoaming.

## Features
- The tools and codes help operators develop their own Passpoint profile provisioning systems.
- The CGI scripts allow end users to download Passpoint profile and configure Wi-Fi without typing in Wi-Fi ID/password or certificate.

## Directory layout
- user: Website with user's login, i.e., with access control.
- ext: Open website where Windows Wi-Fi Settings can download the profile from.
- etc: Storage for configuration and certificate files.

## About WPA2/WPA3 compatibility
The tools are compatible with WPA3. Even if you see WPA2 string in the profiles, it allows Apple and Microsoft devices to join WPA2 or WPA3 networks. Profile for Android (PPS MO) does not have such setting.
