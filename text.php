<?php 
echo "<H1>We did it!</H1>";
$output = shell_exec('pwd');
sleep(10);
echo "<H1>$output</H1>";
?>
