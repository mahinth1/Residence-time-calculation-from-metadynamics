# Residence time calculation from metadynamics
Postprocessing analysis of metadynamics simulation data to estimate protein-ligand complex residence times

**Workflows:** 
1) Running multiple metadynamics simulations (before this analysis)
2) Post-processing
3) Obtaining unbiased dissociation times from each trajectory using PLUMED
4) Fitting for residence times based on cummulative Poisson distribution

![image](https://github.com/user-attachments/assets/969f45ca-db7d-42b5-9bf2-af62bf036d94)

**Required software:** <br/>
-VMD and NAMD (ks.uiuc.edu) <br/>
-PLUMED (https://www.plumed.org)

**Required files:** <br/>
-PDB (coordinates) <br/>
-PSF (structural info) <br/>
-Force field parameter files for MD simulations (i.e., CHARMM) (https://mackerell.umaryland.edu/charmm_ff.shtml) <br/>
-MD simulation trajectories (e.g., dcd, nc, or xtc formats)

**Examples of metadynamics simulations files:** <br/>
simulation_files --> prep <br/>
simulation_files --> metad

Notes: This are just examples from one of simulation sets. You need to go into each individual files to change or specify paths to data or trajectories yourself.

Coordination numbers between the ligand and the binding pocket residues were used in the examples, calculated based on this formula:
![img294](https://github.com/user-attachments/assets/5b90ef88-613f-493e-911a-bebaf26af288)

**Postprocessing analysis steps (after completing metadynamics simulations):**
1) python exittime.py (get the first time frame when the ligand reached the protein surface)
2) (optional) ./trajnowaterlipid (decrease the size of trajectory files by stripping out water and lipids molecules)
3) vmd -dispdev text -e loadframe.tcl (write new trajectory files for analysis)
4) ./runplumed (unbiasing and reweighting using PLUMED: accelerated time --> real time; reweighted free energy profiles)
5) python residencetime.py (fitting for residence times)

# References:
- Tiwary, P.; Parrinello, M. From Metadynamics to Dynamics. Phys. Rev. Lett. 2013, 111, 230602.
- Barducci, A.; Bussi, G.; Parrinello, M. Well-Tempered Metadynamics: A Smoothly Converging and Tunable Free-Energy Method. Phys. Rev. Lett. 2008, 100, 020603.
- Tiwary, P.; Parinnello, M. A Time-Independent Free Energy Estimator from Metadynamics. J. Phys. Chem. B. 2015, 119, 736-742.
- Salvalaglio, M.; Tiwary, P.; Parrinello, M. Assessing the Reliability of the Dynamics Reconstructed from Metadynamics. J. Chem. Theory Comput. 2014, 10, 1420-1425.
- Tribello, G. A.; Bonomi, M.; Branduardi, D.; Camilloni, C.; Bussi, G. PLUMED 2: New Feathers for an Old Bird. Comput. Phys. Commun. 2014, 185, 604-613.
- Fiorin, G.; Klein, M. L.; Hénin, J. Using Collective Variables to Drive Molecular Dynamics Simulations. Mol. Phys. 2013, 111, 3345-3362.
- P. Mahinthichaichan, R. Liu, Q. N. Vo., C. R. Ellis, L. Stavitskaya, J. Shen. Structure-kinetics relationships of opioids from molecular dynamics simulations and machine learning. J. Chem. Info. Model. 2023, 63, 2196-2206.

# Acknowledgements: 
The work is a part of projects in Dr. Yanxin Liu's group at the University of Maryland, College Park (https://blog.umd.edu/liu). 
