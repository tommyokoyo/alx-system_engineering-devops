# using exec to kill a process named killmenow
exec {'killmenow':
    command => 'pkill killmenow',
    path => '/usr/bin',
}
