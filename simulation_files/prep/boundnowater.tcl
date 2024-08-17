#remove water 
package require psfgen
set parameters "/home/mahinthp/paween/ff/toppar"
topology $parameters/top_all36_prot.rtf
topology $parameters/top_all36_na.rtf
topology $parameters/top_all36_lipid.rtf
topology $parameters/top_all36_cgenff.rtf
topology $parameters/toppar_water_ions_for_namd.str
readpsf final.psf
coordpdb final.pdb
delatom X
delatom WT1
delatom WT2
delatom WT3
delatom WT4
delatom WT5
delatom WT6
delatom WT7
delatom WT8
writepsf boundnowater.psf
writepdb boundnowater.pdb


mol delete all
set file [open prot-index.txt w]
mol load psf final.psf pdb final.pdb
set p [atomselect top "protein or resname AAG SOD CLA"]
set index [$p get index]
foreach i $index {puts $file $i}
flush $file
close $file


quit


