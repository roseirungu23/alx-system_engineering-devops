#Puppet manifest containing commands to automatically configure an Ubuntu machine

package { 'nginx':
  ensure => istalled,
}

file_line { 'install':
  ensure => 'present',
  path	 => '/etc/ngix/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx' :
  ensure  => running, 
  require => Package['nginx'],
} 
