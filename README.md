MNIST from Scratch (w/ NumPy)

Why?
    - Learn about the math behind neural networks by doing everything myself.
    - Use as a later reference to create the same project in c++

Project Structure:
neural-network-from-scratch/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ src/
│  └─ mnist_nn.py        # main script (forward/backward/train/eval)
├─ data/                 # (auto-downloaded by Keras)
└─ .venv/                # (not committed)

Requirements:
    numpy >= 1.24.0
    matplotlib >= 3.7.0
    keras >= 3.0.0              # for MNIST data only

Setup:
    git clone <git@github.com:EAHowes/neural-network-from-scratch.git>
    cd neural-network-from-scratch
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt




Activate venv:
source .venv/bin/activate

Deactivate venv:
deactivate


