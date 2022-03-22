# Deep learning detects changes indicative of axial spondyloarthritis on MRI of sacroiliac joints

## Prerequisites
We use our own, openly available library `faimed3d` to build and train neural networks on medical data. `faimed3d` can be installed directly from GitHub with `pip install git+github.com/kbressem/faimed3d`. Alternatively one can also clone the repository and create a symbolic link to the `faimed3d` libs.   
This project is implemented using [`nbdev`](https://nbdev.fast.ai/), a true literate programming environment. 

## Background
Magnetic resonance imaging (MRI) is used for early diagnosis of axial spondyloarthritis (axSpA). Diagnosis of axSpA requires a thorough knowledge of typical imaging findings and experience in rheumatologic imaging, which is challenging for non-specialized centers. Deep learning can facilitate and support diagnosis in clinical practice, but heterogeneity of MRI data and lack of reliable reference standards are important limitations of previous approaches.
We have developed a deep learning tool that enables detection of changes characteristic of axSpA on MRI, overcoming the challenges associated with a large heterogeneous multicenter MRI dataset. 

## Code
All code can be found in the `nbs` folder. The notebooks are sorted chronologically, according to the order in which the methodology is applied in the paper. 

## Paper
TBA
