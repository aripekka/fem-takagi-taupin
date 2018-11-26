# X-ray diffraction profile simulator based on finite element method (FEM) 

COMSOL Multiphysics implementated 2D Takagi-Taupin equation solver in finite element scheme and accompanying Python programs 
for beam propagation computation. For the theoretical background and details, see the literature reference below.

### Contents of the repository

_si111_6keV_0_75_um_grid_source_onrowland_asymmetry.mph_

The newest version of the COMSOL implementation with a capability to compute symmetric and asymmetric Bragg, Laue, and mixed 
diffraction cases. Recommended version.

_si111_6keV_0_75_um_grid_source_onrowland.mph_

As above but limited to the symmetric Bragg case. Used in the computations in the reference below. 

_ttfem_postprocessing.py_

The Python functions to calculate the propagation of the diffracted wavefield.

_example_postprocessing.py_

An example how to use the propagation functions.

_bent_onrowland_6.9697_arcsec.dat_

Example wave data computed with _si111_6keV_0_75_um_grid_source_onrowland.mph_. Used in _example_postprocessing.py_.

_old_version_

The old version of the code with an alternative formulation of the TT-equations for the reference. Less stable than the 
newer versions, and should not be used.

### Quick start

A list of important parameters and variables in _si111_6keV_0_75_um_grid_source_onrowland_asymmetry.mph_.

__Global definitions -> Parameters:__

_width_, _height_ Set the dimensions of the rectangular crystal area

_asymmetry_ Set the asymmetry angle in degrees (0 for symmetric Bragg, 90 for symmetric Laue)

_E0_ The energy of the incident photons

_chi0_,_chih_,_chib_ The relevant Fourier components of the susceptibility. Depend on crystal, reflection, and energy. 
Pay attention to the sign convention

_dhkl_ Separation of the Bragg planes

_FWHM_window_ Full width at half maximum for the Gaussian window of the beam footprint


__Global definitions -> Deformation:__

Currently implemented only for cylindrical deformation.

_R_ The bending radius.

_invR_ The inverse of the bending radius. Set this to 0 to remove the bending.

_nu_ Poisson's ratio

__Global definitions -> Source:__

_source_ Set this to s_cyl\*gaussian_window for diverging source and s_plane\*gaussian_window

_source_distance_ Distance of the diverging source from the origin. No effect to the plane wave source.

__Compute rocking curve -> Parametric sweep:__

For rocking curve calculations or just a single incidence angle, adjust the _scan_arcsec_ parameter here. 
_scan_arcsec_ is relative to the kinematic Bragg's angle.

__Results -> Export -> Waves on surface:__

Use this to export the complex wave amplitudes on the crystal surface for the Python postprocessing and propagation routines. 
Note that the wavenumber and the exit angle, which are also needed, are not exported. 

### Tested COMSOL versions:

Works on COMSOL 5.3a

Doesn't work on COMSOL 4.4

### Literature

Derivative work and publications, please cite our article:

Ari-Pekka Honkanen, Claudio Ferrero, Jean-Pierre Guigay and Vito Mocella
"A finite-element approach to dynamical diffraction problems in reflection geometry"
Journal of Applied Crystallography, 51 (2018), pp. 514-525
DOI: https://doi.org/10.1107/S1600576718001930
Electronic reprint available at https://helda.helsinki.fi/handle/10138/234485
