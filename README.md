# FullStackDataAnalysis
Presentation: Full Stack Data Analysis With Python, February 2015 for Perth Data Science Meetup

**Author**: Jack Golding, reachable at *jackgolding@live.com.au*

View these notebooks at:

http://nbviewer.ipython.org/github/jackgolding/FullStackDataAnalysis/tree/master/

Video of talk at:

https://www.youtube.com/watch?v=N17XGVWAjv8

**Steps**

1. Clone this repo using `git clone https://github.com/jackgolding/FullStackDataAnalysis.git` or by simply downloading the files however you seem fit.
2. Download `Anaconda 2.1` with `Python 3.4` as outlined at http://continuum.io/downloads#34 if Anaconda or Python is updated on continuum's site after this talk has been given you will have to specify the version of Anaconda and/or Python later or risk the code not working.
3. Install Anaconda wherever you want. The beauty of using Anaconda is that deleting it if you don't want it is just a case of deleting the `Anaconda` file after installing.
4. Open a Command Prompt and navigate to the folder you downloaded in Step 1 using `cd FILEPATH` where FILEPATH is the path of the folder.
5. Run `conda create -n FullStack --clone root` if you downloaded Anaconda 2.1 and Python 3 in Sterp 2. If you are using a later version of Python and/or Anaconda you will probably need to run something like `conda create -n FullStack anaconda=2.1.0 python=3.4`
6. Verify the environment you created in `5` exists by running `conda info -e` and noticing you have two environments, `root` and `FullStack`
7. Activate the `FullStack` environment by running `source activate FullStack` - this command may differ depending on what operating system you are using but you should get an useful error message if it doesn't work.
8. To open notebooks run `ipython notebook` to start the IPython Notebook server. 

Please raise any errors as a github issue and star the project if you found it useful.
