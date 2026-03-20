# Awesome Robot Vision

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/han-xudong/awesome-robot-vision?style=social)](https://github.com/han-xudong/awesome-robot-vision/stargazers)

</div>

A curated list of resources for **robot vision** — perception methods, tools, datasets, and benchmarks focused on visual understanding in robotic systems. Covers 6D pose estimation, grasping perception, 3D scene understanding, depth estimation, semantic mapping, visual SLAM, robot learning policies, visual servoing, and related topics.

> ⭐ If you find this list useful, please consider giving it a **star** — it helps others discover the project and motivates continued maintenance!

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a PR.

---

## Contents

- [6D Object Pose Estimation](#6d-object-pose-estimation)
- [Robotic Grasping \& Manipulation Perception](#robotic-grasping--manipulation-perception)
- [Robot Learning Policies with Visual Input](#robot-learning-policies-with-visual-input)
- [3D Perception \& Point Clouds](#3d-perception--point-clouds)
- [Neural Radiance Fields \& Gaussian Splatting](#neural-radiance-fields--gaussian-splatting)
- [Depth Estimation](#depth-estimation)
- [Semantic \& Open-Vocabulary Perception](#semantic--open-vocabulary-perception)
- [Scene Understanding \& Semantic Mapping](#scene-understanding--semantic-mapping)
- [Visual Odometry \& SLAM](#visual-odometry--slam)
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

| Name | Highlights | References |
|---|---|---|
| **[FoundationPose](https://github.com/NVlabs/FoundationPose)** | Unified 6D pose estimation and tracking of novel objects; supports both model-based and model-free setups. **[CVPR 2024 Highlight]** | [GitHub](https://github.com/NVlabs/FoundationPose) · [arXiv](https://arxiv.org/abs/2312.08344) · [Website](https://nvlabs.github.io/FoundationPose/) |
| **[DenseFusion](https://github.com/j96w/DenseFusion)** | Iterative dense fusion of RGB-D data for 6D pose estimation of textureless objects. **[CVPR 2019]** | [GitHub](https://github.com/j96w/DenseFusion) · [arXiv](https://arxiv.org/abs/1901.04780) |
| **[PVN3D](https://github.com/ethnhe/PVN3D)** | Deep point-wise 3D keypoint voting network for 6DoF pose estimation. **[CVPR 2020]** | [GitHub](https://github.com/ethnhe/PVN3D) · [arXiv](https://arxiv.org/abs/1911.04231) |
| **[GDR-Net](https://github.com/THU-DA-6D-Pose-Group/GDR-Net)** | Geometry-guided direct regression network for monocular 6D object pose estimation. **[CVPR 2021]** | [GitHub](https://github.com/THU-DA-6D-Pose-Group/GDR-Net) · [arXiv](https://arxiv.org/abs/2102.12145) |
| **[OnePose](https://github.com/zju3dv/OnePose)** | One-shot object pose estimation without CAD models, using structure-from-motion. **[CVPR 2022]** | [GitHub](https://github.com/zju3dv/OnePose) · [arXiv](https://arxiv.org/abs/2205.12257) |
| **[MegaPose](https://github.com/megapose6d/megapose6d)** | 6D pose estimation of novel objects via render-and-compare at scale. **[CoRL 2022]** | [GitHub](https://github.com/megapose6d/megapose6d) · [arXiv](https://arxiv.org/abs/2212.06174) |
| **[Template-Pose](https://github.com/nv-nguyen/template-pose)** | Template-based 3D object pose estimation revisited for generalization and occlusion robustness. **[CVPR 2022]** | [GitHub](https://github.com/nv-nguyen/template-pose) · [arXiv](https://arxiv.org/abs/2203.05285) |
| **[GigaPose](https://github.com/nv-nguyen/gigapose)** | Fast and robust novel object pose estimation via one correspondence. **[CVPR 2024]** | [GitHub](https://github.com/nv-nguyen/gigapose) · [arXiv](https://arxiv.org/abs/2311.14155) |
| **[CosyPose](https://github.com/ylabbe/cosypose)** | Consistent multi-view multi-object 6D pose estimation from a single image. **[ECCV 2020]** | [GitHub](https://github.com/ylabbe/cosypose) · [arXiv](https://arxiv.org/abs/2008.08465) |
| **[ROMAN](https://github.com/mit-acl/roman)** | View-invariant global localization via open-set object map alignment for robust robot pose estimation. **[RSS 2025]** | [GitHub](https://github.com/mit-acl/roman) · [Website](https://acl.mit.edu/roman) |
| **[Unity Robotics Object Pose Estimation](https://github.com/Unity-Technologies/Robotics-Object-Pose-Estimation)** | End-to-end demonstration of pose estimation from synthetic Unity data for robot pick-and-place. | [GitHub](https://github.com/Unity-Technologies/Robotics-Object-Pose-Estimation) |

### Evaluation & Benchmarks

| Name | Highlights | References |
|---|---|---|
| **[BOP Toolkit](https://github.com/thodan/bop_toolkit)** | Official toolkit for the BOP benchmark: evaluation scripts and utilities for 6D object pose estimation challenges. | [GitHub](https://github.com/thodan/bop_toolkit) · [Website](https://bop.felk.cvut.cz/) |
| **[BOP Challenge](https://bop.felk.cvut.cz/)** | The leading public benchmark for 6D object pose estimation with standardized datasets (LineMOD, T-LESS, YCB-V, etc.) and leaderboards. | [Website](https://bop.felk.cvut.cz/) |

---

## Robotic Grasping & Manipulation Perception

Visual methods for detecting, planning, and evaluating grasp poses; affordance reasoning; and vision for manipulation.

### Grasp Detection & Planning

| Name | Highlights | References |
|---|---|---|
| **[AnyGrasp SDK](https://github.com/graspnet/anygrasp_sdk)** | High-performance, generalizable 6-DoF grasp detection and tracking from point clouds; API for real robot deployment. **[T-RO 2023]** | [GitHub](https://github.com/graspnet/anygrasp_sdk) · [arXiv](https://arxiv.org/abs/2212.08333) · [Website](https://graspnet.net/anygrasp.html) |
| **[GPD](https://github.com/atenpas/gpd)** | Grasp Pose Detection: detects 6-DOF grasp poses in 3D point clouds for robot grasping. **[IJRR 2017]** | [GitHub](https://github.com/atenpas/gpd) · [arXiv](https://arxiv.org/abs/1706.09911) |
| **[GraspNet API](https://github.com/graspnet/graspnetAPI)** | Toolbox and API for the GraspNet-1Billion large-scale grasp pose dataset. **[ICCV 2019]** | [GitHub](https://github.com/graspnet/graspnetAPI) · [Website](https://graspnet.net/) |
| **[GaussianGrasper](https://github.com/MrSecant/GaussianGrasper)** | 3D Language Gaussian Splatting for open-vocabulary robotic grasping from natural language queries. | [GitHub](https://github.com/MrSecant/GaussianGrasper) · [arXiv](https://arxiv.org/abs/2403.09637) · [Website](https://mrsecant.github.io/GaussianGrasper/) |

### Simulation Environments for Manipulation

| Name | Highlights | References |
|---|---|---|
| **[ManiSkill](https://github.com/haosulab/ManiSkill)** | GPU-parallelized robotics simulator and benchmark for manipulation skill learning with rich visual observation. **[ICLR 2024]** | [GitHub](https://github.com/haosulab/ManiSkill) · [Website](https://maniskill.ai/) |
| **[RLBench](https://github.com/stepjam/RLBench)** | Large-scale robot learning benchmark with 100+ diverse manipulation tasks and vision-based observations. **[RA-L 2020]** | [GitHub](https://github.com/stepjam/RLBench) · [Website](https://sites.google.com/view/rlbench) |

---
## Robot Learning Policies with Visual Input

End-to-end visuomotor policies and foundation models for robotic manipulation that use camera observations as primary input.

### Imitation Learning & Diffusion Policies

| Name | Highlights | References |
|---|---|---|
| **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** | Visuomotor policy learning via action diffusion; highly influential framework for robot learning from demonstrations. **[RSS 2023]** | [GitHub](https://github.com/real-stanford/diffusion_policy) · [arXiv](https://arxiv.org/abs/2303.04137) · [Website](https://diffusion-policy.cs.columbia.edu/) |
| **[ACT](https://github.com/tonyzhaozh/act)** | Action Chunking with Transformers: imitation learning policy for bimanual dexterous manipulation from visual observations. **[RSS 2023]** | [GitHub](https://github.com/tonyzhaozh/act) · [arXiv](https://arxiv.org/abs/2304.13705) · [Website](https://tonyzhaozh.github.io/aloha/) |

### Large Robot Foundation Models

| Name | Highlights | References |
|---|---|---|
| **[pi0 / openpi](https://github.com/Physical-Intelligence/openpi)** | Open-source implementation of pi0, a flow-matching-based generalist robot policy with vision-language conditioning. **[CoRL 2024]** | [GitHub](https://github.com/Physical-Intelligence/openpi) · [arXiv](https://arxiv.org/abs/2410.24164) · [Website](https://www.physicalintelligence.company/blog/pi0) |
| **[Octo](https://github.com/octo-models/octo)** | Transformer-based robot policy trained on 800k+ diverse trajectories; supports image, language, and proprioception inputs. **[RSS 2024]** | [GitHub](https://github.com/octo-models/octo) · [arXiv](https://arxiv.org/abs/2405.12213) · [HF](https://huggingface.co/rail-berkeley) |
| **[RT-2](https://github.com/google-research/robotics_transformer)** | Robotics Transformer 2: vision-language-action model trained on web data and robot demonstrations. **[CoRL 2023]** | [GitHub](https://github.com/google-research/robotics_transformer) · [arXiv](https://arxiv.org/abs/2307.15818) |
| **[LeRobot](https://github.com/huggingface/lerobot)** | HuggingFace framework making end-to-end robot learning more accessible; includes datasets, models, and environments. | [GitHub](https://github.com/huggingface/lerobot) · [HF](https://huggingface.co/lerobot) |

---

## 3D Perception & Point Clouds

Libraries and methods for processing 3D sensor data (LiDAR, RGB-D, structured light) in robotic perception pipelines.

### Libraries & Frameworks

| Name | Highlights | References |
|---|---|---|
| **[Open3D](https://github.com/isl-org/Open3D)** | A modern library for 3D data processing: point clouds, meshes, RGBD, registration, visualization, and deep learning integration. | [GitHub](https://github.com/isl-org/Open3D) · [Website](http://www.open3d.org/) |
| **[Point Cloud Library (PCL)](https://github.com/PointCloudLibrary/pcl)** | Foundational open-source library for 2D/3D image and point cloud processing in robotics. **[ICRA 2011]** | [GitHub](https://github.com/PointCloudLibrary/pcl) · [Website](https://pointclouds.org/) |

### Deep Learning on Point Clouds

| Name | Highlights | References |
|---|---|---|
| **[PointNet](https://github.com/fxia22/pointnet.pytorch)** | PyTorch implementation of PointNet: the foundational deep network for 3D point set learning (classification and segmentation). **[CVPR 2017]** | [GitHub](https://github.com/fxia22/pointnet.pytorch) · [arXiv](https://arxiv.org/abs/1612.00593) |
| **[PointNet++](https://github.com/charlesq34/pointnet2)** | Hierarchical feature learning on point sets; improves upon PointNet with local neighborhood grouping. **[NeurIPS 2017]** | [GitHub](https://github.com/charlesq34/pointnet2) · [arXiv](https://arxiv.org/abs/1706.02413) |
| **[MMDetection3D](https://github.com/open-mmlab/mmdetection3d)** | OpenMMLab's next-generation platform for 3D object detection from point clouds (LiDAR and RGB-D). | [GitHub](https://github.com/open-mmlab/mmdetection3d) |

### Registration & Localization

| Name | Highlights | References |
|---|---|---|
| **[TEASER++](https://github.com/MIT-SPARK/TEASER-plusplus)** | Fast and certifiably robust point cloud registration library, robust to high outlier ratios. **[T-RO 2021]** | [GitHub](https://github.com/MIT-SPARK/TEASER-plusplus) · [arXiv](https://arxiv.org/abs/2001.07715) |
| **[Dynamic Robot Localization](https://github.com/carlosmccosta/dynamic_robot_localization)** | Point cloud registration pipeline for robot localization and 3D perception using PCL and ICP/NDT variants. | [GitHub](https://github.com/carlosmccosta/dynamic_robot_localization) |

### Volumetric Reconstruction

| Name | Highlights | References |
|---|---|---|
| **[TSDF Fusion](https://github.com/andyzeng/tsdf-fusion-python)** | Python/CUDA code to fuse multiple RGB-D images into a TSDF voxel volume; widely used for 3D scene reconstruction in manipulation. | [GitHub](https://github.com/andyzeng/tsdf-fusion-python) |

### Gaussian Splatting for Robotics

| Name | Highlights | References |
|---|---|---|
| **[DN-Splatter](https://github.com/maturk/dn-splatter)** | 3D Gaussian splatting with depth and normal priors for improved scene reconstruction from RGB-D. **[3DV 2024]** | [GitHub](https://github.com/maturk/dn-splatter) · [Website](https://maturk.github.io/dn-splatter/) |

---

## Neural Radiance Fields & Gaussian Splatting

Novel implicit and explicit scene representations increasingly used for robot perception, manipulation, and map building.

| Name | Highlights | References |
|---|---|---|
| **[3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)** | Original reference implementation of real-time novel view synthesis via 3D Gaussian primitives; highly influential for robot scene representation. **[ACM ToG / SIGGRAPH 2023]** | [GitHub](https://github.com/graphdeco-inria/gaussian-splatting) · [arXiv](https://arxiv.org/abs/2308.04079) · [Website](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) |
| **[Instant-NGP](https://github.com/NVlabs/instant-ngp)** | Instant neural graphics primitives for lightning-fast NeRF training; enables rapid scene modeling for robotics. **[ACM ToG / SIGGRAPH 2022]** | [GitHub](https://github.com/NVlabs/instant-ngp) · [arXiv](https://arxiv.org/abs/2201.05989) |
| **[Nerfstudio](https://github.com/nerfstudio-project/nerfstudio)** | Collaboration-friendly framework for NeRF and Gaussian splatting methods; modular pipelines for 3D scene reconstruction. **[ACM SIGGRAPH 2023]** | [GitHub](https://github.com/nerfstudio-project/nerfstudio) · [arXiv](https://arxiv.org/abs/2302.04264) · [Website](https://docs.nerf.studio/) |
| **[LERF](https://github.com/kerrj/lerf)** | Language Embedded Radiance Fields: query 3D scenes with natural language using CLIP-grounded NeRFs. **[CoRL 2023]** | [GitHub](https://github.com/kerrj/lerf) · [arXiv](https://arxiv.org/abs/2303.09553) · [Website](https://www.lerf.io/) |
| **[3D-OVS](https://github.com/Kunhao-Liu/3D-OVS)** | Weakly supervised 3D open-vocabulary segmentation from NeRF representations. **[NeurIPS 2023]** | [GitHub](https://github.com/Kunhao-Liu/3D-OVS) · [arXiv](https://arxiv.org/abs/2309.00905) |

---

## Depth Estimation

Methods for recovering metric or relative depth from monocular or stereo cameras, essential for robot spatial reasoning.

### Foundation Models

| Name | Highlights | References |
|---|---|---|
| **[Depth Anything](https://github.com/LiheYoung/Depth-Anything)** | Foundation model for monocular depth estimation trained on large-scale unlabeled data. **[CVPR 2024]** | [GitHub](https://github.com/LiheYoung/Depth-Anything) · [arXiv](https://arxiv.org/abs/2401.10891) · [HF](https://huggingface.co/LiheYoung/depth_anything_vitl14) |
| **[Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)** | Improved foundation model for monocular depth with stronger metric depth capability. **[NeurIPS 2024]** | [GitHub](https://github.com/DepthAnything/Depth-Anything-V2) · [arXiv](https://arxiv.org/abs/2406.09414) · [HF](https://huggingface.co/depth-anything) |
| **[Metric3D](https://github.com/YvanYin/Metric3D)** | Zero-shot metric 3D prediction and versatile monocular geometric foundation model. **[ICCV 2023 · TPAMI 2024]** | [GitHub](https://github.com/YvanYin/Metric3D) · [arXiv](https://arxiv.org/abs/2307.10984) · [HF](https://huggingface.co/spaces/JUGGHM/Metric3D) |
| **[UniDepth](https://github.com/lpiccinelli-eth/UniDepth)** | Universal monocular metric depth estimation from a single image, camera-agnostic. **[CVPR 2024]** | [GitHub](https://github.com/lpiccinelli-eth/UniDepth) · [arXiv](https://arxiv.org/abs/2403.18913) |

### Classic Models

| Name | Highlights | References |
|---|---|---|
| **[MiDaS](https://github.com/isl-org/MiDaS)** | Robust monocular depth estimation via multi-dataset training; widely used for relative depth. **[TPAMI 2022]** | [GitHub](https://github.com/isl-org/MiDaS) · [arXiv](https://arxiv.org/abs/1907.01341) |
| **[MonoDepth2](https://github.com/nianticlabs/monodepth2)** | Self-supervised monocular depth estimation from video; widely cited baseline. **[ICCV 2019]** | [GitHub](https://github.com/nianticlabs/monodepth2) · [arXiv](https://arxiv.org/abs/1806.01260) |

---
## Semantic & Open-Vocabulary Perception

Methods for object detection, segmentation, and language-grounded perception — enabling robots to understand scenes with natural language queries and open-world objects.

### Segmentation

| Name | Highlights | References |
|---|---|---|
| **[Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything)** | Foundation model for promptable image segmentation; broadly applicable in robot perception pipelines. **[ICCV 2023]** | [GitHub](https://github.com/facebookresearch/segment-anything) · [arXiv](https://arxiv.org/abs/2304.02643) · [Website](https://segment-anything.com/) |
| **[SAM 2](https://github.com/facebookresearch/sam2)** | Segment Anything Model 2: real-time promptable segmentation for images and video; stronger and faster than SAM 1. **[ECCV 2024]** | [GitHub](https://github.com/facebookresearch/sam2) · [arXiv](https://arxiv.org/abs/2408.00714) · [Website](https://ai.meta.com/sam2/) |
| **[Grounded-Segment-Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything)** | Combines GroundingDINO and SAM to automatically detect and segment any object from a text prompt. | [GitHub](https://github.com/IDEA-Research/Grounded-Segment-Anything) · [arXiv](https://arxiv.org/abs/2401.14159) |
| **[Mask R-CNN](https://github.com/matterport/Mask_RCNN)** | Classic instance segmentation on Keras/TensorFlow; widely used baseline for robot scene understanding. **[ICCV 2017]** | [GitHub](https://github.com/matterport/Mask_RCNN) · [arXiv](https://arxiv.org/abs/1703.06870) |

### Open-Vocabulary Detection

| Name | Highlights | References |
|---|---|---|
| **[GroundingDINO](https://github.com/IDEA-Research/GroundingDINO)** | Open-set object detection by grounding language queries to image regions. **[ECCV 2024]** | [GitHub](https://github.com/IDEA-Research/GroundingDINO) · [arXiv](https://arxiv.org/abs/2303.05499) |
| **[Detic](https://github.com/facebookresearch/Detic)** | Detecting twenty-thousand classes using image-level supervision; large-vocabulary detection for open-world robot environments. **[ECCV 2022]** | [GitHub](https://github.com/facebookresearch/Detic) · [arXiv](https://arxiv.org/abs/2201.02605) |

### Detection & Segmentation Frameworks

| Name | Highlights | References |
|---|---|---|
| **[Detectron2](https://github.com/facebookresearch/detectron2)** | Facebook AI Research platform for object detection, instance segmentation, and related visual recognition tasks. | [GitHub](https://github.com/facebookresearch/detectron2) |
| **[MMDetection](https://github.com/open-mmlab/mmdetection)** | OpenMMLab detection toolbox covering Faster R-CNN, DETR, YOLO, and 40+ state-of-the-art detectors. | [GitHub](https://github.com/open-mmlab/mmdetection) |
| **[MMSegmentation](https://github.com/open-mmlab/mmsegmentation)** | OpenMMLab semantic segmentation toolbox with 40+ models for outdoor and indoor robot environments. | [GitHub](https://github.com/open-mmlab/mmsegmentation) |
| **[Ultralytics YOLO](https://github.com/ultralytics/ultralytics)** | State-of-the-art real-time object detection, segmentation, pose estimation, and tracking; widely deployed on robot hardware. | [GitHub](https://github.com/ultralytics/ultralytics) · [Website](https://ultralytics.com/) |

### Language-Embedded 3D Representations

See [Neural Radiance Fields & Gaussian Splatting](#neural-radiance-fields--gaussian-splatting) for LERF and 3D-OVS.

---

## Scene Understanding & Semantic Mapping

Methods for building structured, semantic representations of 3D environments for robot navigation and manipulation.

### 3D Scene Graphs

| Name | Highlights | References |
|---|---|---|
| **[Hydra](https://github.com/MIT-SPARK/Hydra)** | Real-time system for building 3D scene graphs from sensor data, enabling hierarchical spatial understanding. **[RSS 2022 · IJRR 2024]** | [GitHub](https://github.com/MIT-SPARK/Hydra) · [Paper](http://www.roboticsproceedings.org/rss18/p050.pdf) |
| **[Khronos](https://github.com/MIT-SPARK/Khronos)** | Spatio-temporal metric-semantic SLAM for tracking dynamic environments with 3D scene graphs. **[RSS 2024]** | [GitHub](https://github.com/MIT-SPARK/Khronos) · [arXiv](https://arxiv.org/abs/2402.13817) |

### Semantic SLAM & Reconstruction

| Name | Highlights | References |
|---|---|---|
| **[Kimera-VIO](https://github.com/MIT-SPARK/Kimera-VIO)** | Visual-inertial odometry with SLAM capabilities, mesh generation, and semantic annotation. **[ICRA 2020]** | [GitHub](https://github.com/MIT-SPARK/Kimera-VIO) · [arXiv](https://arxiv.org/abs/1910.02490) |
| **[Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics)** | Real-time 3D semantic reconstruction from 2D RGB-D images using volumetric mapping. **[ICRA 2020]** | [GitHub](https://github.com/MIT-SPARK/Kimera-Semantics) · [arXiv](https://arxiv.org/abs/1910.02490) |
| **[Voxblox](https://github.com/ethz-asl/voxblox)** | Flexible voxel-based mapping library focused on TSDF and ESDF for robot path planning and obstacle avoidance. **[IROS 2017]** | [GitHub](https://github.com/ethz-asl/voxblox) |
| **[RTAB-Map](https://github.com/introlab/rtabmap)** | Real-Time Appearance-Based Mapping: RGB-D and LiDAR SLAM with loop closure for long-term robot navigation. **[JFR 2019]** | [GitHub](https://github.com/introlab/rtabmap) · [Website](http://introlab.github.io/rtabmap/) |

---

## Visual Odometry & SLAM

Algorithms for estimating robot pose from camera and inertial measurements, enabling autonomous navigation.

### Visual & Visual-Inertial Odometry

| Name | Highlights | References |
|---|---|---|
| **[ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2)** | Real-time SLAM for monocular, stereo, and RGB-D cameras with loop detection and relocalization; one of the most cited SLAM systems. **[T-RO 2017]** | [GitHub](https://github.com/raulmur/ORB_SLAM2) · [arXiv](https://arxiv.org/abs/1610.06475) |
| **[SVO](https://github.com/uzh-rpg/rpg_svo)** | Semi-direct Visual Odometry: combines feature-based and direct methods for fast drone and robot navigation. **[ICRA 2014]** | [GitHub](https://github.com/uzh-rpg/rpg_svo) |
| **[VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)** | Robust and versatile monocular visual-inertial state estimator for aerial robots. **[T-RO 2018]** | [GitHub](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) · [arXiv](https://arxiv.org/abs/1708.03852) |
| **[VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)** | Optimization-based multi-sensor (camera + IMU + GPS) state estimator, extends VINS-Mono. | [GitHub](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) |

### LiDAR Odometry & Mapping

| Name | Highlights | References |
|---|---|---|
| **[LIO-SAM](https://github.com/TixiaoShan/LIO-SAM)** | Tightly-coupled LiDAR-inertial odometry via smoothing and mapping; widely used for ground robot localization. **[IROS 2020]** | [GitHub](https://github.com/TixiaoShan/LIO-SAM) · [arXiv](https://arxiv.org/abs/2007.00258) |

### SLAM Back-Ends & Factor Graphs

| Name | Highlights | References |
|---|---|---|
| **[GTSAM](https://github.com/borglab/gtsam)** | Georgia Tech Smoothing and Mapping library: factor graph-based back-end for SLAM and sensor fusion, used extensively in robotics research. | [GitHub](https://github.com/borglab/gtsam) · [Website](https://gtsam.org/) |

---

## Feature Matching

Local feature detectors and matchers used in robot pose estimation, object recognition, and visual localization.

| Name | Highlights | References |
|---|---|---|
| **[LightGlue](https://github.com/cvg/LightGlue)** | Fast and accurate local feature matching via adaptive transformer-based matching. **[ICCV 2023]** | [GitHub](https://github.com/cvg/LightGlue) · [arXiv](https://arxiv.org/abs/2306.13643) |
| **[SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork)** | Learning feature matching with graph neural networks; widely used for visual localization in robotics. **[CVPR 2020]** | [GitHub](https://github.com/magicleap/SuperGluePretrainedNetwork) · [arXiv](https://arxiv.org/abs/1911.11763) |

---

## Optical Flow & Scene Flow

Estimating pixel-level or point-level motion from image sequences, used for robot motion understanding and dynamic obstacle tracking.

| Name | Highlights | References |
|---|---|---|
| **[RAFT](https://github.com/princeton-vl/RAFT)** | Recurrent All-Pairs Field Transforms for optical flow; state-of-the-art baseline widely adopted in robotics. **[ECCV 2020]** | [GitHub](https://github.com/princeton-vl/RAFT) · [arXiv](https://arxiv.org/abs/2003.12039) |
| **[RAFT-3D](https://github.com/princeton-vl/RAFT-3D)** | Extension of RAFT to scene flow estimation from RGB-D, enabling 3D motion understanding. **[CVPR 2021]** | [GitHub](https://github.com/princeton-vl/RAFT-3D) · [arXiv](https://arxiv.org/abs/2012.00726) |

---

## Visual Servoing & Active Perception

Methods for controlling robot motion using visual feedback, and for actively choosing viewpoints to improve perception quality.

### Visual Servoing

| Name | Highlights | References |
|---|---|---|
| **[ViSP](https://github.com/lagadic/visp)** | Open Source Visual Servoing Platform: comprehensive library for image-based (IBVS) and position-based (PBVS) visual servoing with ROS support. | [GitHub](https://github.com/lagadic/visp) · [Website](https://visp.inria.fr/) |

---

## Simulation & Benchmarks

Simulation environments and evaluation benchmarks for robot vision tasks.

### Benchmarks

| Name | Highlights | References |
|---|---|---|
| **[BOP Challenge](https://bop.felk.cvut.cz/)** | Annual benchmark for 6D object pose estimation with standardized datasets, metrics (ADD, VSD, MSSD, MSPD), and public leaderboards. | [Website](https://bop.felk.cvut.cz/) |
| **[BOP Toolkit](https://github.com/thodan/bop_toolkit)** | Scripts for evaluation, rendering, and dataset handling for BOP benchmark datasets. | [GitHub](https://github.com/thodan/bop_toolkit) |
| **[GraspNet-1Billion](https://graspnet.net/)** | Large-scale benchmark for general object grasping with 97,280 RGB-D images, 1 billion grasp annotations, and evaluation tools. **[ICCV 2019]** | [Website](https://graspnet.net/) |

### Simulators

| Name | Highlights | References |
|---|---|---|
| **[ManiSkill](https://github.com/haosulab/ManiSkill)** | GPU-parallelized robotic manipulation simulator with photo-realistic rendering and diverse manipulation tasks. **[ICLR 2024]** | [GitHub](https://github.com/haosulab/ManiSkill) · [Website](https://maniskill.ai/) |
| **[RLBench](https://github.com/stepjam/RLBench)** | Large-scale robot learning environment with 100+ manipulation tasks and multiple visual camera viewpoints. **[RA-L 2020]** | [GitHub](https://github.com/stepjam/RLBench) · [Website](https://sites.google.com/view/rlbench) |
| **[DM Control](https://github.com/google-deepmind/dm_control)** | Google DeepMind's physics-based simulation suite using MuJoCo for robot learning environments. | [GitHub](https://github.com/google-deepmind/dm_control) |

---

## Datasets

Curated datasets for training and evaluating robot vision models.

### Object Pose Estimation Datasets

| Dataset | Description | Publication | Link |
|---|---|---|---|
| **LineMOD** | 13 low-textured household objects with 6D pose annotations; foundational benchmark for pose estimation | ACCV 2012 | [Project](http://campar.in.tum.de/Main/StefanHinterstoisser) |
| **T-LESS** | 30 industry-relevant textureless objects in cluttered scenes; part of BOP | WACV 2017 | [Project](http://cmp.felk.cvut.cz/t-less/) |
| **YCB-Video** | 21 YCB objects with RGB-D video sequences and 6D pose annotations for manipulation | CVPR 2018 | [Project](https://rse-lab.cs.washington.edu/projects/posecnn/) |
| **HomebrewedDB** | 33 objects with complex geometry, multiple lighting, real and synthetic images; part of BOP | ICCVW 2019 | [BOP Page](https://bop.felk.cvut.cz/datasets/) |
| **HOPE-Video** | Household objects for pose estimation from video, addressing temporal consistency | — | [GitHub](https://github.com/swtyree/hope-dataset) |
| **YCBV (BOP)** | YCB objects in BOP format with standardized splits; benchmark for manipulation | — | [BOP Page](https://bop.felk.cvut.cz/datasets/) |

### Grasp Datasets

| Dataset | Description | Publication | Link |
|---|---|---|---|
| **GraspNet-1Billion** | 97,280 RGB-D images of 88 objects with 1.19B annotated grasp poses | ICCV 2019 | [Project](https://graspnet.net/) |
| **Cornell Grasping Dataset** | 885 images with 8,019 labeled grasps; standard 2D grasp rectangle benchmark | ICRA 2011 | [Dataset](http://pr.cs.cornell.edu/grasping/rect_data/data.php) |
| **Jacquard** | Large-scale synthetic grasp dataset with 54K images and accurate depth maps | IROS 2018 | [Project](https://jacquard.liris.cnrs.fr/) |

### Scene Understanding Datasets

| Dataset | Description | Publication | Link |
|---|---|---|---|
| **ScanNet** | 1,513 annotated RGB-D indoor scans with 3D object labels; widely used for scene understanding and 3D detection | CVPR 2017 | [Project](http://www.scan-net.org/) / [GitHub](https://github.com/ScanNet/ScanNet) |
| **Matterport3D** | 90 building-scale RGB-D scans with region and object annotations for navigation | 3DV 2017 | [Project](https://niessner.github.io/Matterport/) |
| **OCID** | Object Clutter Indoor Dataset: cluttered tabletop scenes with instance segmentation labels | IROS 2019 | [Dataset](https://www.acin.tuwien.ac.at/en/vision-for-robotics/software-tools/object-clutter-indoor-dataset/) |
| **HM3D** | Habitat-Matterport 3D: 1,000 building-scale 3D environments for embodied navigation agents | NeurIPS 2021 | [Project](https://aihabitat.org/datasets/hm3d/) |

---

## Toolkits & Libraries

General-purpose libraries and ROS packages for building robot vision systems.

### Computer Vision Foundations

| Name | Highlights | References |
|---|---|---|
| **[OpenCV](https://github.com/opencv/opencv)** | The foundational open-source computer vision library with comprehensive support for image processing, camera calibration, and feature detection. | [GitHub](https://github.com/opencv/opencv) · [Website](https://opencv.org/) |
| **[OpenCV Contrib](https://github.com/opencv/opencv_contrib)** | Extra modules for OpenCV including aruco markers, surface matching, and other robotics-relevant tools. | [GitHub](https://github.com/opencv/opencv_contrib) |

### Pose & Keypoint Estimation Frameworks

| Name | Highlights | References |
|---|---|---|
| **[MMPose](https://github.com/open-mmlab/mmpose)** | OpenMMLab pose estimation toolbox supporting human, hand, animal, and general keypoint detection. | [GitHub](https://github.com/open-mmlab/mmpose) |

### Calibration

| Name | Highlights | References |
|---|---|---|
| **[Kalibr](https://github.com/ethz-asl/kalibr)** | Visual-inertial calibration toolbox for camera intrinsics, camera-IMU extrinsics, and multi-camera rigs; essential for robot sensor setup. **[IROS 2012]** | [GitHub](https://github.com/ethz-asl/kalibr) |

### Annotation

| Name | Highlights | References |
|---|---|---|
| **[Labelme](https://github.com/wkentaro/labelme)** | Image annotation tool supporting polygon, rectangle, and AI-assisted labeling; widely used to create robot vision training data. | [GitHub](https://github.com/wkentaro/labelme) |

### ROS Integration

| Name | Highlights | References |
|---|---|---|
| **[vision_opencv](https://github.com/ros-perception/vision_opencv)** | Official ROS packages bridging OpenCV and ROS for image transport and processing in robot pipelines. | [GitHub](https://github.com/ros-perception/vision_opencv) |
| **[image_pipeline](https://github.com/ros-perception/image_pipeline)** | ROS image processing pipeline: camera drivers, rectification, stereo, and depth image tools. | [GitHub](https://github.com/ros-perception/image_pipeline) |

### Deployment & Inference

| Name | Highlights | References |
|---|---|---|
| **[torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)** | Easy-to-use PyTorch to TensorRT converter for deploying robot vision models on NVIDIA edge hardware (Jetson). | [GitHub](https://github.com/NVIDIA-AI-IOT/torch2trt) |
| **[CuRobo](https://github.com/NVlabs/curobo)** | CUDA-accelerated robot library for GPU-parallel motion generation and collision checking, used with vision-based perception. | [GitHub](https://github.com/NVlabs/curobo) · [arXiv](https://arxiv.org/abs/2310.17274) · [Website](https://curobo.org/) |

---

## Surveys

Overview and survey papers that provide a structured view of robot vision sub-fields.

| Title | Description | Venue | Link |
|---|---|---|---|
| **A Survey on Deep Learning Approaches for 6D Object Pose Estimation** | Covers model-based and model-free methods, datasets, metrics, and trends. | arXiv 2022 | [arXiv](https://arxiv.org/abs/2009.10378) |
| **Robotic Grasping from Classical to Modern: A Survey** | Comprehensive review of grasp planning from analytical to data-driven deep learning methods. | arXiv 2023 | [arXiv](https://arxiv.org/abs/2202.03631) |
| **A Survey on Monocular Depth Estimation** | Covers supervised, self-supervised, and foundation model approaches. | arXiv 2024 | [arXiv](https://arxiv.org/abs/2401.17512) |
| **Open-Vocabulary Object Detection: A Survey** | Reviews VLM-based approaches for open-set detection applicable to robotics. | arXiv 2024 | [arXiv](https://arxiv.org/abs/2401.11739) |
| **3D Scene Graph: A Structure for Unified Semantics, 3D Space, and Camera** | Foundational paper for 3D scene graphs in robot understanding. | ICCV 2019 | [Website](https://3dscenegraph.stanford.edu/) |


---

## License

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers of **Awesome Robot Vision** have waived all copyright and related or neighboring rights to this work. This list is released to the public domain under the [CC0 1.0 Universal](LICENSE) license — you are free to copy, modify, and distribute the content without asking permission.
