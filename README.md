MNIST from Scratch (w/ NumPy)  

Why?  
    - Learn about the math behind neural networks by doing everything myself.  
    - Use as a later reference to create the same project in c++  
  
Project Structure:  
neural-network-from-scratch/    
├── data  
├── README.md  
├── requirements.txt  
└── src  
    ├── __init__.py  
    └── mnist_nn.py  
  
Requirements:  
    numpy==2.3.4  
    matplotlib==3.10.7  
    keras==3.11.3        # for MNIST data only  
  
Setup:  
    git clone <git@github.com:EAHowes/neural-network-from-scratch.git>  
    cd neural-network-from-scratch  
    python3 -m venv .venv  
    source .venv/bin/activate  
    pip install -U pip  
    pip install -r requirements.txt  
