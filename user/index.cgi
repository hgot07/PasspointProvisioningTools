#!/usr/bin/perl

use CGI;
my $q = CGI->new();

my $ua = $ENV{'HTTP_USER_AGENT'};

# Auto OS detection
my $detOS = 'none';
if ( $ua =~ /Windows/ ){
	if ( $ua !~ /phone/ ){
		$detOS = 'Windows';
	}
}
elsif ( $ua =~ /Mac/ && $ua =~ /OS/ ){
	$detOS = 'macOS';
	if ( $ua =~ /iPhone/ || $ua =~ /iPad/ || $ua =~ /iPod/ ){
		$detOS = 'iOS';
	}
}
elsif ( $ua =~ /Android/ ){
	$detOS = 'Android';
}
elsif ( $ua =~ /CrOS/ ){
	$detOS = 'ChromeOS';
}

print <<"EOS";
Content-Type: text/html; charset=utf-8

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
<title>User Menu</title>
</head>
<body>
<h1>User Menu (example)</h1>

<ul>
EOS

if ( $detOS eq 'Android' ) {
print <<"EOS";
<li><a href="passpoint-android.config">Auto-detected: <strong>Android</strong></a> (recommended)</li>
EOS
}
elsif ( $detOS eq 'macOS' ){
print <<"EOS";
<li><a href="passpoint.mobileconfig.cgi">Auto-detected: <strong>macOS</strong></a> (recommended)</li>
EOS
}
elsif ( $detOS eq 'iOS' ){
print <<"EOS";
<li><a href="passpoint.mobileconfig.cgi">Auto-detected: <strong>iOS/iPadOS</strong></a> (recommended)</li>
EOS
}
elsif ( $detOS eq 'Windows' ){
print <<"EOS";
<li><a href="ppwin-helper.cgi">Auto-detected: <strong>Windows</strong></a> (recommended)</li>
EOS
}
else{
	print "<li>Auto-detected: <strong>none</strong> &nbsp;(no supported OS is found)</li>\n";
}

print <<"EOS";
<br>
<li>Manual selection:</li>
<ul>
<li><a href="passpoint-android.config">Android 10+</a></li>
<li><a href="passpoint.mobileconfig.cgi">iOS/iPadOS 14+, macOS 10+</a></li>
<li><a href="ppwin-helper.cgi">Windows 11 22H2+</a></li>
<!--
<br>
<li><a href="passpoint.eap-config.cgi">Download Passpoint profile in eap-config format (OS-independent)</a><br>
Please use
<a href="https://www.geteduroam.app/" target="_blank" rel="norefferrer">geteduroam</a> to configure user devices using this profile.</li>
-->
</ul>
</body>
</html>
EOS

1;
