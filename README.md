# ai-prompt-to-image-generator

![Demo](https://cdn.sanjaysikdar.dev/assets/ai-prompt-to-image-generator/demo-1.png)


Demo Video: https://youtu.be/iz-YDlU6j4Y

## Stack

Python: 3.12.3

Flask: 3.0.3

## How to Run?

-   Clone or download [ai-prompt-to-image-generator](https://github.com/sannjayy/ai-prompt-to-image-generator)

`git clone git@github.com:sannjayy/ai-prompt-to-image-generator.git`

-   Create a virtual environment

```bash
python -m venv zenv
source zenv/Scripts/activate # Windows
source zenv/bin/activate # Mac
```

-   Install basic requirements

```bash
pip install -r requirements.txt

# OR INITIAL INSTALLATION

pip install --upgrade pip
pip install --upgrade setuptools

pip install transformers diffusers flask pillow
```

-   Install PyTorch ([CUDA](https://pytorch.org/get-started/locally/))

```bash
# CUDA 12.1 (Windows)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# CUDA 11.1 (Windows)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# MAC
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu

# OR (Others)
pip install torch torchvision
```

### To Run

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser!

---

---

-   🌏 [GitHub Repo](https://github.com/sannjayy/ai-prompt-to-image-generator)
-   🌏 [Website](https://www.sanjaysikdar.dev)
-   📫 <me@sanjaysikdar.dev>
-   📖 [read.sanjaysikdar.dev](https://read.sanjaysikdar.dev)
-   📦 [pypi releases](https://pypi.org/user/sannjayy/) | [npm releases](https://www.npmjs.com/~sannjayy)

---

[![](https://img.shields.io/github/followers/sannjayy?style=social)](https://github.com/sannjayy)  
Developed with ❤️ by _[sanjaysikdar.dev](https://www.sanjaysikdar.dev)_.
