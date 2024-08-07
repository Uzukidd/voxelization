import os

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

if __name__ == '__main__':

    setup(
        name='voxel_ops',
        packages=find_packages(exclude = ["test", "data"]),
        cmdclass={
            'build_ext': BuildExtension,
        },
        ext_modules=[
           CUDAExtension(
                name='voxel_ops._ext_voxel_ops',
                sources=[
                    'voxel_ops/ext-src/scatter_points_cpu.cpp',
                    'voxel_ops/ext-src/scatter_points_cuda.cu',
                    'voxel_ops/ext-src/voxelization_cpu.cpp',
                    'voxel_ops/ext-src/voxelization_cuda.cu',
                    'voxel_ops/ext-src/voxelization.cpp',
                ],
                include_dirs=[
                    'voxel_ops/ext-src/voxelization.h',
                ],
                define_macros=[
                    ('WITH_CUDA', None),
                ],
                
            )
        ],
    )