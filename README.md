# srsRAN_docs
Documentation for the srsRAN project - see [docs.srsran.com](http://docs.srsran.com)

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
git clone https://github.com/srsRAN/srsRAN_docs.git
cd srsRAN_docs/srsran_user_manuals
make html
```

Then load the compiled doc in your browser
```
firefox build/html/index.html
google-chrome build/html/index.html
```
