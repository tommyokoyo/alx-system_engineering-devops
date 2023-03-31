#installs flask from pip3
package{'flask':
    enusre => '2.1.0',
    provider => 'pip3',
}
