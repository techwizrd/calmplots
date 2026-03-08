Quickstart
==========

Install
-------

For most users:

.. code-block:: bash

   pip install calmplots

To include all optional backend integrations:

.. code-block:: bash

   pip install "calmplots[all]"

For local development with `uv`:

.. code-block:: bash

   uv sync --extra all

Apply themes
------------

.. code-block:: python

   import calmplots

   calmplots.apply_matplotlib_theme()
   calmplots.set_seaborn_theme(context="notebook")
   calmplots.register_plotly_template(set_default=True)
   calmplots.enable_altair_theme()

Plotnine example
----------------

.. code-block:: python

   from plotnine import aes, geom_point, ggplot
   import pandas as pd
   from calmplots import scale_color_calm, theme_calm

   df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [2, 3, 2, 5], "grp": ["a", "b", "a", "b"]})

   p = (
       ggplot(df, aes("x", "y", color="grp"))
       + geom_point(size=3)
       + scale_color_calm()
       + theme_calm()
   )
