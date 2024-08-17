##calculate solvent accessible surface area of ligand (e.g. AAG)
set n [molinfo top get numframes]
set o [open ./run${f}/sasalig.dat w]

puts $o "#! FIELDS time sasa maxsasa nsasa"
for {set i 0} {$i < $n} {incr i} {
	set prot [atomselect top "protein or resname AAG" frame $i] 
	set lig [atomselect top "resname AAG" frame $i]
	set sasa [measure sasa 1.4 $prot -restrict $lig]
	set sasalig [measure sasa 1.4 $lig]
        set norm [expr $sasa / $sasalig] 
	puts $o "$i $sasa $sasalig $norm"
}
close $o
