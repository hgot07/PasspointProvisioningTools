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

CGI scripts require execution handler,
 e.g. "AddHandler cgi-script .cgi .config" in case of Apache2 web server.

## About WPA2/WPA3 compatibility
These tools are compatible with WPA3. Even if you see WPA2 string in the profiles, it allows Apple and Microsoft devices to join WPA2 or WPA3 networks. Profile for Android (PPS MO) does not have such setting.

## EAP-TLS support status
These tools support EAP-TLS on the following operating systems.
- Android
- iOS/iPadOS
- macOS

Unfortunately, Windows does not support EAP-TLS setting
 through the ms-settings: URI scheme as of Oct. 2024.
- cf. [Overview of Passpoint (Hotspot 2.0) in Windows](https://github.com/MicrosoftDocs/windows-driver-docs/blob/staging/windows-driver-docs-pr/mobilebroadband/passpoint.md)

A workaround is as follows, but this is cumbersome.
1. Operator issues a Passpoint profile for the EAP-TTLS method and 
 a client certificate in PKCS #12 format.
1. User configures the device through the web-based provisioning 
 and loads the client certificate manually.
1. User changes the Wi-Fi setting to EAP-TLS mode from EAP-TTLS manually.

Note that the EAP-TLS (RFC 5216) is not always so secure in terms of privacy.
Access Network Providers can snoop into the contents of client certificates.
A workaround is to use "EAP-TTLS with EAP-TLS as inner method".
Some supplicants like wpa_supplicant and Windows support this configuration,
 but the ms-settings: URI scheme does not work as explained above.

