#!C:\xampp\perl\bin\perl.exe
use strict;
use warnings;

# Open employee details file
open my $fh, "<", "employee_details.txt" or die "Cannot open employee details file: $!";

# Initialize variables
my $total_tax = 0;
my $html_output = <<END;
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Employee Income Tax Summary</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
  <style>
    body {
      font-family: 'Open Sans', sans-serif;
      background-color: #f7f7f7;
    }
    h2 {
      color: #333;
      font-size: 28px;
      text-align: center;
      margin-top: 40px;
      box-shadow: #353232 0px 7px 30px;
      border-radius:10px;
      padding:10px;
      margin-left:15rem;
      margin-right:15rem;
    }
    table {
      margin: 40px auto;
      border-collapse: collapse;
      border: 1px solid #ccc;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    }
    th, td {
      padding: 10px 15px;
      border-bottom: 1px solid #ccc;
      text-align: center;
    }
    th {
      background-color: #f2f2f2;
    }
    tr:hover {
      background-color: #f5f5f5;
    }
    .total {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h2>Employee Income Tax Summary</h2>
  <table>
    <tr>
      <th>Name</th>
      <th>Salary</th>
      <th>Tax</th>
    </tr>
END

# Loop through employee details
while (my $line = <$fh>) {
    chomp $line;
    my ($name, $emp_no, $salary, $pan, $password) = split /,/, $line;
    my $tax = calculate_tax($salary);
    $total_tax += $tax;
    $html_output .= "<tr><td>$name</td><td>$salary</td><td>$tax</td></tr>";
}

# Close employee details file
close $fh;

# Add total tax to output
$html_output .= "<tr class='total'><th>Total Tax:</th><td></td><td>$total_tax</td></tr></table></body></html>";

# Print HTML output
print "Content-type: text/html\n\n$html_output";

# Subroutine to calculate tax
sub calculate_tax {
    my $salary = shift;
    my $tax = 0;
    if ($salary > 50000) {
        $tax = $salary * 0.2;
    } elsif ($salary > 30000) {
        $tax = $salary * 0.15;
    } else {
        $tax = $salary * 0.1;
    }
  return $tax;
}
