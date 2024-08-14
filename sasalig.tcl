
#for {set f 0 } {$f < 3} {incr f} {

#mol load psf /scratch/Liu_Group/paween/hsp90/hsp90/1yet_unsat/prep_17aag/boundnowater.psf
#mol addfile ./run${f}/rewrap.dcd waitfor all 
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
#mol delete all
#} 
