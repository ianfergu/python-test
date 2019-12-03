<?php 
echo "<H1>We did it!</H1>";
$output = shell_exec('ssh fabian@http://comp535-lnx-lampvm1.cs.unc.edu/');
sleep(10);
echo "<H1>$output</H1>";
?>
