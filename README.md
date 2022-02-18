# Dimer-Generator

Generate various dimer configuarations by rotating and translating the monomers. Completely written in Python 3.

### Features
- Calculate center of mass and move the monomer to center of mass
- Translate the duplicate monomer along all directions
- Rotate the duplicate monomer about all axes


### Usage
- Run the `run.py` file with input file as the first argument. The program will ask you to input the necessary information for the transformations.
```bash
python run.py input1.xyz
```

### Few important points
- Note that the outputs are rounded of to the 5th decimal place
- Note that the program only supports .xyz files as input right now (for example, see ```input0.xyz```). 
- Support for more extensions will be added soon!

### Requirements
- NumPy
- Pandas
- [Mendeleev](https://pypi.org/project/mendeleev/)

Install the required packages using

```bash
pip install -r requirements.txt
```

If you find a bug, drop me an email.

You are welcome to contribute to the project! Please fork the repo and submit a pull request.

#### Author Info:
[Ajay Melekamburath](https://ajay-mk/github.io)

ajaymk16@iisertvm.ac.in

Follow me: 
[Github](https://github.com/ajay-mk) | [Twitter](https://twitter.com/ajay-mk)
