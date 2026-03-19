# Awesome Robot Vision [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of resources for **robot vision** — perception methods, tools, datasets, and benchmarks focused on visual understanding in robotic systems. Covers 6D pose estimation, grasping perception, 3D scene understanding, depth estimation, semantic mapping, visual servoing, and related topics.

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

## Contents

- [6D Object Pose Estimation](#6d-object-pose-estimation)
- [Robotic Grasping \& Manipulation Perception](#robotic-grasping--manipulation-perception)
- [3D Perception \& Point Clouds](#3d-perception--point-clouds)
- [Depth Estimation](#depth-estimation)
- [Semantic \& Open-Vocabulary Perception](#semantic--open-vocabulary-perception)
- [Scene Understanding \& Semantic Mapping](#scene-understanding--semantic-mapping)
- [Feature Matching](#feature-matching)
- [Optical Flow \& Scene Flow](#optical-flow--scene-flow)
- [Visual Servoing \& Active Perception](#visual-servoing--active-perception)
- [Simulation \& Benchmarks](#simulation--benchmarks)
- [Datasets](#datasets)
- [Toolkits \& Libraries](#toolkits--libraries)
- [Surveys](#surveys)

---

## 6D Object Pose Estimation

Methods and frameworks for estimating the 6-DoF (3D position + 3D orientation) of objects from images or point clouds, a core capability for robot manipulation.

### Methods

- **[FoundationPose](https://github.com/NVlabs/FoundationPose)** — Unified 6D pose estimation and tracking of novel objects; supports both model-based and model-free setups. CVPR 2024 Highlight. ![Stars](https://img.shields.io/github/stars/NVlabs/FoundationPose?style=flat-square)
- **[DenseFusion](https://github.com/j96w/DenseFusion)** — Iterative dense fusion of RGB-D data for 6D pose estimation of textureless objects. CVPR 2019. ![Stars](https://img.shields.io/github/stars/j96w/DenseFusion?style=flat-square)
- **[PVN3D](https://github.com/ethnhe/PVN3D)** — Deep point-wise 3D keypoint voting network for 6DoF pose estimation. CVPR 2020. ![Stars](https://img.shields.io/github/stars/ethnhe/PVN3D?style=flat-square)
- **[GDR-Net](https://github.com/THU-DA-6D-Pose-Group/GDR-Net)** — Geometry-guided direct regression network for monocular 6D object pose estimation. CVPR 2021. ![Stars](https://img.shields.io/github/stars/THU-DA-6D-Pose-Group/GDR-Net?style=flat-square)
- **[OnePose](https://github.com/zju3dv/OnePose)** — One-shot object pose estimation without CAD models, using structure-from-motion. CVPR 2022. ![Stars](https://img.shields.io/github/stars/zju3dv/OnePose?style=flat-square)
- **[MegaPose](https://github.com/megapose6d/megapose6d)** — 6D pose estimation of novel objects via render-and-compare at scale. CoRL 2022. ![Stars](https://img.shields.io/github/stars/megapose6d/megapose6d?style=flat-square)
- **[Template-Pose](https://github.com/nv-nguyen/template-pose)** — Template-based 3D object pose estimation revisited for generalization and occlusion robustness. CVPR 2022. ![Stars](https://img.shields.io/github/stars/nv-nguyen/template-pose?style=flat-square)
- **[GigaPose](https://github.com/nv-nguyen/gigapose)** — Fast and robust novel object pose estimation via one correspondence. CVPR 2024. ![Stars](https://img.shields.io/github/stars/nv-nguyen/gigapose?style=flat-square)
- **[ROMAN](https://github.com/mit-acl/roman)** — View-invariant global localization via object matching for robust robot pose estimation. RSS 2025. ![Stars](https://img.shields.io/github/stars/mit-acl/roman?style=flat-square)
- **[Unity Robotics Object Pose Estimation](https://github.com/Unity-Technologies/Robotics-Object-Pose-Estimation)** — End-to-end demonstration of pose estimation from synthetic Unity data for robot pick-and-place. ![Stars](https://img.shields.io/github/stars/Unity-Technologies/Robotics-Object-Pose-Estimation?style=flat-square)

### Evaluation & Benchmarks

- **[BOP Toolkit](https://github.com/thodan/bop_toolkit)** — Official toolkit for the BOP benchmark: evaluation scripts and utilities for 6D object pose estimation challenges. ![Stars](https://img.shields.io/github/stars/thodan/bop_toolkit?style=flat-square)
- **[BOP Challenge](https://bop.felk.cvut.cz/)** — The leading public benchmark for 6D object pose estimation with standardized datasets (LineMOD, T-LESS, YCB-V, etc.) and leaderboards.

---

## Robotic Grasping & Manipulation Perception

Visual methods for detecting, planning, and evaluating grasp poses; affordance reasoning; and vision for manipulation.

### Grasp Detection & Planning

- **[AnyGrasp SDK](https://github.com/graspnet/anygrasp_sdk)** — High-performance, generalizable 6-DoF grasp detection from point clouds; API for real robot deployment. ![Stars](https://img.shields.io/github/stars/graspnet/anygrasp_sdk?style=flat-square)
- **[GPD](https://github.com/atenpas/gpd)** — Grasp Pose Detection: detects 6-DOF grasp poses in point clouds for robot grasping. ![Stars](https://img.shields.io/github/stars/atenpas/gpd?style=flat-square)
- **[GraspNet API](https://github.com/graspnet/graspnetAPI)** — Toolbox and API for the GraspNet-1Billion large-scale grasp pose dataset. ![Stars](https://img.shields.io/github/stars/graspnet/graspnetAPI?style=flat-square)

### Simulation Environments for Manipulation

- **[ManiSkill](https://github.com/haosulab/ManiSkill)** — GPU-parallelized robotics simulator and benchmark for manipulation skill learning with rich visual observation. ![Stars](https://img.shields.io/github/stars/haosulab/ManiSkill?style=flat-square)

---

## 3D Perception & Point Clouds

Libraries and methods for processing 3D sensor data (LiDAR, RGB-D, structured light) in robotic perception pipelines.

### Libraries & Frameworks

- **[Open3D](https://github.com/isl-org/Open3D)** — A modern library for 3D data processing: point clouds, meshes, RGBD, registration, visualization, and deep learning integration. ![Stars](https://img.shields.io/github/stars/isl-org/Open3D?style=flat-square)
- **[Point Cloud Library (PCL)](https://github.com/PointCloudLibrary/pcl)** — Foundational open-source library for 2D/3D image and point cloud processing in robotics. ![Stars](https://img.shields.io/github/stars/PointCloudLibrary/pcl?style=flat-square)

### Registration & Localization

- **[TEASER++](https://github.com/MIT-SPARK/TEASER-plusplus)** — Fast and certifiably robust point cloud registration library, robust to high outlier ratios. ![Stars](https://img.shields.io/github/stars/MIT-SPARK/TEASER-plusplus?style=flat-square)
- **[Dynamic Robot Localization](https://github.com/carlosmccosta/dynamic_robot_localization)** — Point cloud registration pipeline for robot localization and 3D perception using PCL and ICP/NDT variants. ![Stars](https://img.shields.io/github/stars/carlosmccosta/dynamic_robot_localization?style=flat-square)

### Gaussian Splatting for Robotics

- **[DN-Splatter](https://github.com/maturk/dn-splatter)** — 3D Gaussian splatting with depth and normal priors for robot-relevant scene reconstruction from RGB-D. ![Stars](https://img.shields.io/github/stars/maturk/dn-splatter?style=flat-square)

---

## Depth Estimation

Methods for recovering metric or relative depth from monocular or stereo cameras, essential for robot spatial reasoning.

### Foundation Models

- **[Depth Anything](https://github.com/LiheYoung/Depth-Anything)** — Foundation model for monocular depth estimation trained on large-scale unlabeled data. CVPR 2024. ![Stars](https://img.shields.io/github/stars/LiheYoung/Depth-Anything?style=flat-square)
- **[Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)** — Improved foundation model for monocular depth with stronger metric depth capability. NeurIPS 2024. ![Stars](https://img.shields.io/github/stars/DepthAnything/Depth-Anything-V2?style=flat-square)
- **[Metric3D](https://github.com/YvanYin/Metric3D)** — Zero-shot metric 3D prediction and versatile monocular geometric foundation model. ![Stars](https://img.shields.io/github/stars/YvanYin/Metric3D?style=flat-square)
- **[UniDepth](https://github.com/lpiccinelli-eth/UniDepth)** — Universal monocular metric depth estimation from a single image, camera-agnostic. ![Stars](https://img.shields.io/github/stars/lpiccinelli-eth/UniDepth?style=flat-square)

### Classic Models

- **[MiDaS](https://github.com/isl-org/MiDaS)** — Robust monocular depth estimation via multi-dataset training; widely used for relative depth. TPAMI 2022. ![Stars](https://img.shields.io/github/stars/isl-org/MiDaS?style=flat-square)
- **[MonoDepth2](https://github.com/nianticlabs/monodepth2)** — Self-supervised monocular depth estimation from video; widely cited baseline. ICCV 2019. ![Stars](https://img.shields.io/github/stars/nianticlabs/monodepth2?style=flat-square)

---

## Semantic & Open-Vocabulary Perception

Methods for object detection, segmentation, and language-grounded perception — enabling robots to understand scenes with natural language queries and open-world objects.

### Segmentation

- **[Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything)** — Foundation model for promptable image segmentation; broadly applicable in robot perception pipelines. ICCV 2023. ![Stars](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square)
- **[Grounded-Segment-Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything)** — Combines GroundingDINO and SAM to automatically detect and segment any object from a text prompt. ![Stars](https://img.shields.io/github/stars/IDEA-Research/Grounded-Segment-Anything?style=flat-square)

### Open-Vocabulary Detection

- **[GroundingDINO](https://github.com/IDEA-Research/GroundingDINO)** — Open-set object detection by grounding language queries to image regions. ECCV 2024. ![Stars](https://img.shields.io/github/stars/IDEA-Research/GroundingDINO?style=flat-square)

### Detection & Segmentation Frameworks

- **[Detectron2](https://github.com/facebookresearch/detectron2)** — Facebook AI Research platform for object detection, instance segmentation, and related visual recognition tasks. ![Stars](https://img.shields.io/github/stars/facebookresearch/detectron2?style=flat-square)

### Language-Embedded 3D Representations

- **[LERF](https://github.com/kerrj/lerf)** — Language Embedded Radiance Fields: query 3D scenes with natural language using CLIP-grounded NeRFs. ![Stars](https://img.shields.io/github/stars/kerrj/lerf?style=flat-square)
- **[3D-OVS](https://github.com/Kunhao-Liu/3D-OVS)** — Weakly supervised 3D open-vocabulary segmentation from NeRF representations. NeurIPS 2023. ![Stars](https://img.shields.io/github/stars/Kunhao-Liu/3D-OVS?style=flat-square)

---

## Scene Understanding & Semantic Mapping

Methods for building structured, semantic representations of 3D environments for robot navigation and manipulation.

### 3D Scene Graphs

- **[Hydra](https://github.com/MIT-SPARK/Hydra)** — Real-time system for building 3D scene graphs from sensor data, enabling hierarchical spatial understanding. ![Stars](https://img.shields.io/github/stars/MIT-SPARK/Hydra?style=flat-square)
- **[Khronos](https://github.com/MIT-SPARK/Khronos)** — Spatio-temporal metric-semantic SLAM for tracking dynamic environments with 3D scene graphs. ![Stars](https://img.shields.io/github/stars/MIT-SPARK/Khronos?style=flat-square)

### Semantic SLAM & Reconstruction

- **[Kimera-VIO](https://github.com/MIT-SPARK/Kimera-VIO)** — Visual-inertial odometry with SLAM capabilities, mesh generation, and semantic annotation. ![Stars](https://img.shields.io/github/stars/MIT-SPARK/Kimera-VIO?style=flat-square)
- **[Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics)** — Real-time 3D semantic reconstruction from 2D RGB-D images using volumetric mapping. ![Stars](https://img.shields.io/github/stars/MIT-SPARK/Kimera-Semantics?style=flat-square)
- **[Voxblox](https://github.com/ethz-asl/voxblox)** — Flexible voxel-based mapping library focused on TSDF and ESDF for robot path planning and obstacle avoidance. ![Stars](https://img.shields.io/github/stars/ethz-asl/voxblox?style=flat-square)

---

## Feature Matching

Local feature detectors and matchers used in robot pose estimation, object recognition, and visual localization.

- **[LightGlue](https://github.com/cvg/LightGlue)** — Fast and accurate local feature matching via adaptive transformer-based matching. ICCV 2023. ![Stars](https://img.shields.io/github/stars/cvg/LightGlue?style=flat-square)
- **[SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork)** — Learning feature matching with graph neural networks; widely used for visual localization in robotics. CVPR 2020. ![Stars](https://img.shields.io/github/stars/magicleap/SuperGluePretrainedNetwork?style=flat-square)

---

## Optical Flow & Scene Flow

Estimating pixel-level or point-level motion from image sequences, used for robot motion understanding and dynamic obstacle tracking.

- **[RAFT](https://github.com/princeton-vl/RAFT)** — Recurrent All-Pairs Field Transforms for optical flow; state-of-the-art baseline widely adopted in robotics. ECCV 2020. ![Stars](https://img.shields.io/github/stars/princeton-vl/RAFT?style=flat-square)
- **[RAFT-3D](https://github.com/princeton-vl/RAFT-3D)** — Extension of RAFT to scene flow estimation from RGB-D, enabling 3D motion understanding. CVPR 2021. ![Stars](https://img.shields.io/github/stars/princeton-vl/RAFT-3D?style=flat-square)

---

## Visual Servoing & Active Perception

Methods for controlling robot motion using visual feedback, and for actively choosing viewpoints to improve perception quality.

### Visual Servoing

- **[ViSP](https://github.com/lagadic/visp)** — Open Source Visual Servoing Platform: comprehensive library for image-based (IBVS) and position-based (PBVS) visual servoing with ROS support. ![Stars](https://img.shields.io/github/stars/lagadic/visp?style=flat-square)

---

## Simulation & Benchmarks

Simulation environments and evaluation benchmarks for robot vision tasks.

### Benchmarks

- **[BOP Challenge](https://bop.felk.cvut.cz/)** — Annual benchmark for 6D object pose estimation with standardized datasets, metrics (ADD, VSD, MSSD, MSPD), and public leaderboards.
- **[BOP Toolkit](https://github.com/thodan/bop_toolkit)** — Scripts for evaluation, rendering, and dataset handling for BOP benchmark datasets. ![Stars](https://img.shields.io/github/stars/thodan/bop_toolkit?style=flat-square)
- **[GraspNet-1Billion](https://graspnet.net/)** — Large-scale benchmark for general object grasping with 97,280 RGB-D images, 1 billion grasp annotations, and evaluation tools.

### Simulators

- **[ManiSkill](https://github.com/haosulab/ManiSkill)** — GPU-parallelized robotic manipulation simulator with photo-realistic rendering and diverse manipulation tasks. ![Stars](https://img.shields.io/github/stars/haosulab/ManiSkill?style=flat-square)

---

## Datasets

Curated datasets for training and evaluating robot vision models.

### Object Pose Estimation Datasets

| Dataset | Description | Link |
|---|---|---|
| **LineMOD** | 13 low-textured household objects with 6D pose annotations; foundational benchmark for pose estimation | [Project](http://campar.in.tum.de/Main/StefanHinterstoisser) |
| **T-LESS** | 30 industry-relevant textureless objects in cluttered scenes; part of BOP | [Project](http://cmp.felk.cvut.cz/t-less/) |
| **YCB-Video** | 21 YCB objects with RGB-D video sequences and 6D pose annotations for manipulation | [Project](https://rse-lab.cs.washington.edu/projects/posecnn/) |
| **HomebrewedDB** | 33 objects with complex geometry, multiple lighting, real and synthetic images; part of BOP | [BOP Page](https://bop.felk.cvut.cz/datasets/) |
| **HOPE-Video** | Household objects for pose estimation from video, addressing temporal consistency | [GitHub](https://github.com/swtyree/hope-dataset) |
| **YCBV (BOP)** | YCB objects in BOP format with standardized splits; benchmark for deformable-free manipulation | [BOP Page](https://bop.felk.cvut.cz/datasets/) |

### Grasp Datasets

| Dataset | Description | Link |
|---|---|---|
| **GraspNet-1Billion** | 97,280 RGB-D images of 88 objects with 1.19B annotated grasp poses | [Project](https://graspnet.net/) |
| **Cornell Grasping Dataset** | 885 images with 8,019 labeled grasps; standard 2D grasp rectangle benchmark | [Dataset](http://pr.cs.cornell.edu/grasping/rect_data/data.php) |
| **Jacquard** | Large-scale synthetic grasp dataset with 54K images and accurate depth maps | [Project](https://jacquard.liris.cnrs.fr/) |

### Scene Understanding Datasets

| Dataset | Description | Link |
|---|---|---|
| **ScanNet** | 1,513 annotated RGB-D indoor scans with 3D object labels; widely used for scene understanding | [Project](http://www.scan-net.org/) |
| **Matterport3D** | 90 building-scale RGB-D scans with region and object annotations for navigation | [Project](https://niessner.github.io/Matterport/) |
| **OCID** | Object Clutter Indoor Dataset: cluttered tabletop scenes with instance segmentation labels | [GitHub](https://github.com/atenpas/gpd) |

---

## Toolkits & Libraries

General-purpose libraries and ROS packages for building robot vision systems.

### Computer Vision Foundations

- **[OpenCV](https://github.com/opencv/opencv)** — The foundational open-source computer vision library with comprehensive support for image processing, camera calibration, and feature detection. ![Stars](https://img.shields.io/github/stars/opencv/opencv?style=flat-square)
- **[OpenCV Contrib](https://github.com/opencv/opencv_contrib)** — Extra modules for OpenCV including aruco markers, surface matching, and other robotics-relevant tools. ![Stars](https://img.shields.io/github/stars/opencv/opencv_contrib?style=flat-square)

### ROS Integration

- **[vision_opencv](https://github.com/ros-perception/vision_opencv)** — Official ROS packages bridging OpenCV and ROS for image transport and processing in robot pipelines. ![Stars](https://img.shields.io/github/stars/ros-perception/vision_opencv?style=flat-square)

### Deployment & Inference

- **[torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)** — Easy-to-use PyTorch to TensorRT converter for deploying robot vision models on NVIDIA edge hardware (Jetson). ![Stars](https://img.shields.io/github/stars/NVIDIA-AI-IOT/torch2trt?style=flat-square)

---

## Surveys

Overview and survey papers that provide a structured view of robot vision sub-fields.

- **A Survey on Deep Learning Approaches for 6D Object Pose Estimation** — Covers model-based and model-free methods, datasets, metrics, and trends. [arXiv 2022](https://arxiv.org/abs/2009.10378)
- **Robotic Grasping from Classical to Modern: A Survey** — Comprehensive review of grasp planning from analytical to data-driven deep learning methods. [arXiv 2023](https://arxiv.org/abs/2202.03631)
- **A Survey on Monocular Depth Estimation** — Covers supervised, self-supervised, and foundation model approaches. [arXiv 2024](https://arxiv.org/abs/2401.17512)
- **Open-Vocabulary Object Detection: A Survey** — Reviews VLM-based approaches for open-set detection applicable to robotics. [arXiv 2024](https://arxiv.org/abs/2401.11739)
- **3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera** — Foundational paper for 3D scene graphs in robot understanding. [ICCV 2019](https://3dscenegraph.stanford.edu/)
- **Deep Learning for Visual Perception in Robotics** — Broad overview of deep learning methods across the core robot vision tasks. [Annual Review of Control, Robotics, and Autonomous Systems 2023](https://www.annualreviews.org/doi/10.1146/annurev-control-042920-013838)

---

## Contributing

Contributions are welcome! Please:
1. Check that the resource is relevant to **robot vision** (not general CV or robotics without a strong vision component).
2. Add the resource to the appropriate section in alphabetical order where possible.
3. Include the GitHub star badge for code repositories.
4. For papers, include the venue/year and a link.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related or neighboring rights to this work.
