Python-only healpy
==================

Stripped down hacked version of `healpy` with only map-loading and plotting capabilities.

Install the package with:

        pip install .

Test that it can visualize a map:

        python test_healpyvis.py

Check it creates `map.png` file.

# Building PyHealpy with JupyterLite's Pyodide

by @VeerioSDSC

Steps include building the wheel to serve, setting up JupyterLite, and commands for the Lite cells. 

### Building the PyHealpy Wheel to Serve

First need to set up the pyodide compiler with the following

```
pip install pyodide-build
git clone https://github.com/emscripten-core/emsdk.git
cd emsdk
PYODIDE_EMSCRIPTEN_VERSION=$(pyodide config get emscripten_version)
./emsdk install ${PYODIDE_EMSCRIPTEN_VERSION}
./emsdk activate ${PYODIDE_EMSCRIPTEN_VERSION}
source emsdk_env.sh
cd ..
```

Then building the wheel:

```
git clone https://github.com/healpy/pyhealpy.git
cd pyhealpy
pyodide build
```
It builds the wheel in a dist folder

Serving the wheel locally:

`python3 -m http.server --directory dist`

### Using it with JupyterLite

If one just wants to use another environment they can use the demo one found here: https://jupyterlite.github.io/demo/lab/index.html

If one wants to deploy Lite with GitHub Pages:

Template to use: https://github.com/jupyterlite/demo
Since the initial commit will fail, go to settings→actions→general and allow read/write perms for workflows, and go to settings→pages and make sure GitHub Actions is selected as the source for Deployment. Make a commmit and then it will deploy. 

If one wants to deploy Lite locally:

```
python -m pip install jupyterlite-core
jupyter lite init
python3 -m pip install jupyterlite-pyodide-kernel
cd _output
jupyter lite build
jupyter lite serve
```
### Commands to Run in JupyterLite - web address for installation is based on where the wheel is served. 

If locally, you might face [CORS Issue. ](https://chromewebstore.google.com/detail/moesif-origincors-changer/digfbfaphojjndkpccljibejjbppifbc?hl=en-US)

Commands for the cells:

```
import micropip
await micropip.install ("http://localhost:8000/healpy-0.1.dev1885+g71d9336-py3-none-any.whl") 
await micropip.install("matplotlib")
import healpy
```

Then it can be tested with the [contents of file from above](https://github.com/healpy/pyhealpy/blob/pyhealpy/test_healpyvis.py):

```

import healpy as hp
import matplotlib.pyplot as plt

m = hp.read_map(
    "wmap_band_iqumap_r9_7yr_W_v4_udgraded32_masked_smoothed10deg_fortran.fits"
);
#link will change based on where file is 

hp.projview(m, coord=["G"], projection_type="mollweide");

plt.savefig("map.png")
```


