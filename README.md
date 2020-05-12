# srsLTE_docs
Documentation for the srsLTE project - see [docs.srslte.com](http://docs.srslte.com)

# Local Installation 

The docs require following Sphinx extensions:
- sphinxcontrib-seqdiag
- sphinxcontrib-blockdiag

On Ubuntu, they can be installed with:
```
sudo apt install python-pip
pip install sphinx sphinx_rtd_theme sphinxcontrib.blockdiag sphinxcontrib.seqdiag
```

Once dependenceies are installed,

```
git clone https://github.com/srsLTE/srsLTE_docs.git
srsLTE_docs/srslte_user_manuals
make html
```

Then load the compiled doc in your browser
```
firefox build/html/index.html
google-chrome build/html/index.html
```
