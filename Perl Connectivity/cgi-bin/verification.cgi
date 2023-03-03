v#!C:\xampp\perl\bin\perl.exe
use strict;
use warnings;

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

my $file = "employee_details.txt";

# Get user input
my $user_id = param('user_id');
my ($password) = param('password');

# Check if user ID and password match
open my $fh, '<', $file or die "Cannot open $file: $!";
while (my $line = <$fh>) {
    chomp $line;
    my ($name, $emp_no, $salary, $pan_no, $stored_password) = split /, /, $line;
    if ($pan_no eq $user_id && $stored_password eq $password) {
        print "Content-type: text/html\n\n";
        print "<html><head><title>Authorization Successful</title>";
        print "<style>body { font-family: Arial, sans-serif; background-color: #f2f2f2; }";
        print "h2 { color: #009933; }";
        print "p { color: #666666; }";
        print "button { background-color: #009933; color: #ffffff; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px; }";
        print "</style></head>";
        print "<body>";
        print "<h2>Authorization Successful!!!</h2>";
        print "<p>Welcome $name. Your monthly salary is Rs. $salary.</p>";
        print "<button onclick=\"location.href='/summary.html'\">View Summary</button>";
        print "</body></html>";
        exit;
    }
}
close $fh;

# If user ID and password do not match
print "Content-type: text/html\n\n";
print "<html><head><title>Authorization Failed</title>";
print "<style>body { font-family: Arial, sans-serif; background-color: #f2f2f2; }";
print "h2 { color: #ff0000; }";
print "p { color: #666666; }";
print "button { background-color: #009933; color: #ffffff; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px; }";
print "</style></head>";
print "<body>";
print "<h2>Authorization Failed!</h2>";
print "<p>Please enter correct User ID and Password.</p>";
print "<button onclick=\"location.href='/index.html'\">Retry</button>";
print "</body></html>";



