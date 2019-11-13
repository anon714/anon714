# ARFlow

**This repo and account are part of the supplementary material for anonymous submission, so I do not accept any PR or issue currently. Everything will be moved to the official account in time.**

## Requirements

This code has been developed under Python3, PyTorch 1.1.0 and CUDA 9.0 on Ubuntu 16.04. 

We strongly recommend that using docker in your environment to ensure that you can get the same results as us. The [Dockerfile](./Dockerfile) is available. 

Otherwise, you can also build the environment by following:

### Minimal dependencies for Inference

The python packages can be installed with

```shell
pip3 install -r requirements.txt
```

Then, install the correlation package:

```shell
cd ./models/correlation_package
python3 setup.py install
```

If you have any trouble with this package, we also provide an alternative implementation. You can modify the import lines in `models/pwclite.py` to use it.

### Additional dependencies for Training

TBA

## Pre-trained Models

The `checkpoints` folder contains the final models of ARFlow and ARFlow-mv for MPI Sintel, KITTI12, KITTI15 and Cityscapes. Additional models for ablation are available upon request.

## Using the Code

### Inference

For two-view models, just run with:

```shell
python3 inference.py -m checkpoints/KITTI15/pwclite_ar.tar -s 384 640 \
  -i examples/img1.png examples/img2.png
```

For multi-view model, input with 3 frames:

```shell
python3 inference.py -m checkpoints/KITTI15/pwclite_ar_mv.tar -s 384 640 \
  -i examples/img0.png examples/img1.png examples/img2.png
```

We recommend input with 384x640 for KITTI and Cityscapes models, 448x1024 for Sintel models.

### Training
#### Datasets for training：

Due to copyright issues, please download the dataset from the official websites.

- [MPI Sintel Dataset](http://sintel.is.tue.mpg.de/downloads) and [Sintel Original Movie](https://www.youtube.com/watch?v=eRsGyueVLvQ)
- [KITTI Raw](http://www.cvlibs.net/datasets/kitti/raw_data.php), [KITTI 2015](http://www.cvlibs.net/download.php?file=data_scene_flow_multiview.zip), [KITTI 2012](http://www.cvlibs.net/download.php?file=data_stereo_flow_multiview.zip)
- [FlyingChairs](https://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs.en.html#flyingchairs), [CityScapes](https://www.cityscapes-dataset.com/downloads/) 

If you have any trouble about creating the Sintel Raw dataset, please open an issue after the paper is accepted.

#### Training on the Standard Optical Flow Benchmarks

Will be released once the paper is accepted.

#### Training on the Custom Video Datasets

Will be released once the paper is accepted.

## License

TBA

## Citation

TBA