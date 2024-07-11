import healpy as hp

m = hp.read_map(
    "healpy/test/data/wmap_band_iqumap_r9_7yr_W_v4_udgraded32_masked_smoothed10deg_fortran.fits"
);

hp.projview(m, coord=["G"], projection_type="mollweide");
