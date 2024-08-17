
mol load psf boundnowater.psf pdb boundnowater.pdb
set file [open mc.txt w]
set all [atomselect top "all"]
$all writepdb plumed.pdb
set n [$all num]
set range []
for {set i 0 } {$i<$n} {incr i} {lappend range $i}
set m [$all get mass]
set c [$all get charge]
puts $file "#! FIELDS index mass charge"

foreach i $range m0 $m c0 $c {puts $file "$i $m0 $c0"}
flush $file
close $file

quit

