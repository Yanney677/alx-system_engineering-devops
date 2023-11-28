#!/usr/bin/env bash
# Using puppet to make changes to our configuration file

file { 'ect/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentication no
	",
}
