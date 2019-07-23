# srsLTE_docs
Documentation for the srsLTE project - see [docs.srslte.com](http://docs.srslte.com)

# Local Installation 

The docs require following Sphinx extensions:
- sphinxcontrib-seqdiag
- sphinxcontrib-blockdiag

On Ubuntu, they can be installed with:

$ sudo apt-get install sphinxcontrib-autoprogram python-sphinxcontrib.blockdiag python-sphinxcontrib.seqdiag python-pip
$ pip install sphinx_rtd_theme

Once it's done, navigate to, e.g.,

$ google-chrome build/html/index.html
