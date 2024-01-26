#Puppet
user { 'John':
  ensure   => present,
  home     => "~",
  provider => "shell"
}
