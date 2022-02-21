# Dimer-Generator

Generate various dimer configuarations by rotating and translating the monomers. Completely written in Python 3.

### Features
- Calculate center of mass and move the monomer to center of mass
- Translate the duplicate monomer along all directions
- Rotate the duplicate monomer about all axes
- Save the dimer geometry in a .xyz file


### Usage

#### Running run_interactive.py
- Run the `run_interactive.py` file with input file as the first argument. The program will ask you to input the necessary information for the transformations.
```bash
python run.py input_samples/input1.xyz
```

#### Running run_args.py
- Run the run_args.py with the following arguments:
  
    -i , --input_file       Input file in xyz format

    -c , --com_to_origin       Specify if centre of mass is translated to origin (y/n) (default: n)

    -t , --translate       Input translation direction

    -td , --translation_distance       Input translation distance

    -r , --rotate       Input rotation axis

    -ra , --rotation_angle       Input rotation angle
- For example:
  ```bash
    python run_args.py -i input_samples/input1.xyz -c y -t x -td 1.0 -r y -ra 90.0
  ```
- The output geometry is saved into `INPUT_FILENAME_dimer.xyz` file by default.
- Run `python run_args.py -h` or `python run_args.py --help` for more information.


### Few important points
- Note that the `translation_distance` is defined as the distance between the centre of masses of monomers.
- Note that the outputs are rounded of to the 5<sup>th</sup> decimal place
- Note that the program only supports .xyz files as input and output right now (for examples, see `input_samples`).
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
