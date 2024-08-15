# Residence-time-calculation-from-metadynamics
Postprocessing analysis of metadynamics simulation data to estimate protein-ligand complex residence times

Workflows
Multiple metadynamics simulations (before this analysis) --> Post-processing --> Unbiased dissociation times (PLUMED) --> Fitting for residence times

Software: VMD and PLUMED (visualization and analysis) ; NAMD with Colvars Modules (MD simulations)

Required files: PDB (coordinates) and PSF (structural info); MD simulation trajectories (e.g., dcd, nc, or xtc formats)

Notes: This is just an example from one of simulation sets. You need to go into each individual files to change or specify paths to data or trajectories yourself.

Steps (after completing metadynamics simulations):
1) python exittime.py (get first frame when the ligand reached the protein surface)
2) (optional) ./trajnowaterlipid (decrease the size of trajectory files by stripping out water and lipids molecules)
3) vmd -dispdev text -e loadframe.tcl (write new trajectory files for analysis)
4) ./runplumed (unbiasing and reweighting using PLUMED: accelerated time --> real time; reweighted free energy profiles)
5) python residencetime.py (compute residence times)


# Acknowledgements: 
The work is a part of projects in Dr. Yanxin Liu's group at the University of Maryland, College Park (https://blog.umd.edu/liu)
