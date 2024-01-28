# A scripts that fix the number of failed requests to get to 0
exec { 'change ULIMIT':
  command => "sed -i 's/15/4096/g' /etc/default/nginx ; service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
