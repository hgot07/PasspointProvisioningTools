#!/usr/bin/perl
#
# Passpoint Provisioning Tools
#  Helper for Windows Passpoint profile provisioning
# 
# Usage:
#  - Run Redis server.
#  - Put this script in a resricted directory where an access control
#    is effective by Basic Authentication, etc.
#  - Adjust the URL so that it points to your own main CGI script
#    (passpoint-win.config).
#  - Modify the way how to get the ID of the accessed user.
# Notes:
#  - This script will pass the user ID (REMOTE_USER, etc.) 
#    to the main script using a random key through Redis.
#  - See also the main script passpoint-win.config.
#
# 20220729 Hideaki Goto (Cityroam/eduroam)
# 20230118 Hideaki Goto (Cityroam/eduroam)	+ Script URI auto-setting
#

use String::Random;
use Redis;

$confCGI = "ms-settings:wifi-provisioning?uri=https://$ENV{'HTTP_HOST'}$ENV{'REQUEST_URI'}";
$confCGI =~ s/user\/ppwin-helper.cgi/ext\/passpoint-win.config/;

$TTL = 60;

my $sr = String::Random->new();
$key = $sr->randregex('[a-zA-Z0-9]{20}');

my $redis = Redis->new(server => 'localhost:6379') or die;
$uid = $ENV{'REMOTE_USER'};

$redis->set($key, "$uid", 'EX', $TTL);

print << "EOS";
Content-Type: text/html

<head>
<meta http-equiv="refresh" content="0;URL=$confCGI?ukey=$key">
</head>
<body>
<ul>
<li> <a href="$confCGI?ukey=$key">Download Wi-Fi profile.</a> (within $TTL sec.)
</ul>
</body>
EOS

exit(0);
