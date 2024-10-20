# PasspointProvisioningTools
Tools and example codes for Passpoint profile provisioning, mainly for OpenRoaming. Only EAP-TTLS is supported. If you want to use EAP-TLS, you need to write your own code. Some OSs may not support EAP-TLS.

## Features
- The tools and codes help operators develop their own Passpoint profile provisioning systems.
- The CGI scripts allow end users to download Passpoint profile and configure Wi-Fi without typing in Wi-Fi ID/password or certificate.

## Directory layout
- user: Website with user's login, i.e., with access control.
- ext: Open website where Windows Wi-Fi Settings can download the profile from.
- etc: Storage for configuration and certificate files.

## Requirements
Redis or compatible server is needed on the same host.

## About WPA2/WPA3 compatibility
These tools are compatible with WPA3. Even if you see WPA2 string in the profiles, it allows Apple and Microsoft devices to join WPA2 or WPA3 networks. Profile for Android (PPS MO) does not have such setting.
