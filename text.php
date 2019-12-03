<?php 
echo "<n>We did it!</n>";
$output = shell_exec('ssh fabian@http://comp535-lnx-lampvm1.cs.unc.edu/');
echo "<pre>$output</pre>";
?>
