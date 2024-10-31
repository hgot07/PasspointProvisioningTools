#!/usr/bin/perl

sub getuserinfo {
	my $webuser = $_[0];

# Write your own code here to set per-user parameters.
	#$userID = 'name@example.com';
	#$passwd = 'nicePassword';
	#$ExpirationDate = '2023-01-05T00:00:00Z';


	# The scripts issue EAP-TLS profiles
	#  when $client_cert(_np) is non-empty.

	# Client Certificate for EAP-TLS (Android, etc.)
	# (Base64 enc., PKCS #12 containing client cert.&key, w/o passwd)
	#$client_cert_np = '';

	# Client Certificate for EAP-TLS (macOS, etc.)
	# (Base64 enc., PKCS #12 containing client cert.&key, with passwd)
	#$client_cert = '';
	#$client_cert_pass = '';

	# SHA256 fingerprint of the Client Certificate
	#$client_hash = '01:02:03:...';

	return(0);
}

1;
