#
#  This file is part of Healpy.
#
#  Healpy is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Healpy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Healpy; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#  For more information about Healpy, see http://code.google.com/p/healpy
#
"""HealPy is a package to manipulate Healpix maps (ang2pix, pix2ang) and
compute spherical harmonics tranforms on them.
"""

from .version import __version__

from .pixelfunc import (
    ma,
    mask_good,
    mask_bad,
    ang2pix,
    pix2ang,
    xyf2pix,
    pix2xyf,
    pix2vec,
    vec2pix,
    vec2ang,
    ang2vec,
    nside2npix,
    npix2nside,
    nside2order,
    order2nside,
    order2npix,
    npix2order,
    isnsideok,
    isnpixok,
    ring2nest,
    nest2ring,
    reorder,
    get_all_neighbours,
    max_pixrad,
    get_interp_val,
    get_interp_weights,
    fit_dipole,
    fit_monopole,
    remove_dipole,
    remove_monopole,
    get_nside,
    maptype,
    ud_grade,
    nside2resol,
    nside2pixarea,
    get_map_size,
)

from .rotator import Rotator, vec2dir, dir2vec
from .visufunc import (
    mollview,
    graticule,
    delgraticules,
    gnomview,
    projplot,
    projscatter,
    projtext,
    cartview,
    orthview,
    azeqview,
)
from .newvisufunc import projview, newprojplot
from .zoomtool import mollzoom, set_g_clim
from .fitsfunc import write_map, read_map, read_alm, write_alm, write_cl, read_cl


from .utils.deprecation import deprecated


@deprecated("1.15.0")
def disable_warnings():
    """healpy uses logging now

    This function has no effect
    """
    pass


@deprecated("1.15.0")
def enable_warnings():
    """healpy uses logging now

    This function has no effect
    """
    pass
