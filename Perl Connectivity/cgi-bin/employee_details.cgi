#!C:\xampp\perl\bin\perl.exe
use strict;
use warnings;

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

# Get form data
my $name = param('name');
my $emp_no = param('emp_no');
my $salary = param('salary');
my $pan = param('pan');
my $password = param('password');

# Open file for writing
open(my $fh, '>>', 'employee_details.txt') or die "Cannot open file: $!";

# Write data to file
print $fh "$name, $emp_no, $salary, $pan, $password\n";

# Close file
close $fh;

# Display success message
print header,
      start_html(
        -title => 'Employee Details Submitted',
        -style => {
          -src => 'https://fonts.googleapis.com/css?family=Open+Sans',
          -type => 'text/css'
        }
      ),
      style('
        body {
          font-family: "Open Sans", sans-serif;
          background-color: #f2f2f2;
          text-align: center;
        }
        h1 {
          font-size: 2.5rem;
          margin-top: 2rem;
          color:green
        }
        a.back-btn {
            background-image: linear-gradient(
          to bottom right,
          #ff5833d2,
          rgb(252, 136, 106)
        );
        padding-left: 16px;
        padding-right: 16px;
        padding-top: 8px;
        padding-bottom: 8px;
        border-radius: 10px;
        color: black;
        font-size: 1rem;
        font-weight: 500;
        box-shadow: #353232 0px 7px 30px;
}

        a.back-btn:hover {
             background-color: #3e8e41;
}
       
      '),
      h1('Employee details submitted successfully.'),
      a({-href => '/index.html', -class => 'back-btn'}, 'Login'),
end_html;