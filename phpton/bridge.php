<?php
$output=null;
$retval=null;
exec('python3 -c "__import__(\'sys\').path.insert(0, \'@phpton_dir@\'); import phpton; phpton.load(\'@script_path@\'); phpton.run(\'' . $_SERVER['REQUEST_URI'] . '\')"', $output, $retval);
foreach($output as $line) {
    echo $line;
}
?>
