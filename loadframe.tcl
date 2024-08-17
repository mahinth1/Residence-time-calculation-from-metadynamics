###Generate new dcd files for PLUMED analysis ####
###20 simulation runs ###
for {set f 0 } {$f < 20} {incr f } {

set in [open exittime.dat r]
set dat [ split [read $in ] "\n"]
set lastframe [lindex $dat $f 2]

    #input psf file
    mol load psf boundnowater.psf
    #input trajectory file
    mol addfile ./run${f}/traj.dcd last ${lastframe} waitfor all
    package require pbctools
    pbc unwrap -sel "protein"
    pbc wrap  -compound residue -sel "not protein" -center com -centersel "protein" -all
    set n [molinfo top get numframes]
    #protein residues as references for alignment
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
 
