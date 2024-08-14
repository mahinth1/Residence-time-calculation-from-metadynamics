###Generate new dcd files for PLUMED analysis ####
###20 simulation runs ###
for {set f 0 } {$f < 20} {incr f } { 

set in [open exittime.dat r]
set dat [ split [read $in ] "\n"]
set lastframe [lindex $dat $f 2] 

    mol load psf /scratch/Liu_Group/paween/hsp90/hsp90/1yet_unsat/prep_17aag/boundnowater.psf 
    mol addfile ./run${f}/traj.dcd last ${lastframe} waitfor all
    package require pbctools
    pbc unwrap -sel "protein"
    pbc wrap  -compound residue -sel "not protein" -center com -centersel "protein" -all
    set n [molinfo top get numframes]
    for {set i 0} {$i < $n} {incr i} {
    set ref [atomselect top "protein and name CA and resid 20 to 94 146 to 220" frame 0]
    set sel [atomselect top "protein and name CA and resid 20 to 94 146 to 220" frame $i]
    set all [atomselect top "all" frame $i ] 
    $all move [measure fit $sel $ref]

    source sasalig.tcl

    }

    set all [atomselect top "all"]
    animate write dcd ./run${f}/rewrap.dcd waitfor all sel $all

    mol delete all
}
quit
 
