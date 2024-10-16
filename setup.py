from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='pointpillars',
    version='0.1',
    packages=find_packages(),
    ext_modules=[
        CUDAExtension(
            name='pointpillars.ops.voxel_op',
            sources=[
                'pointpillars/ops/voxelization/voxelization.cpp',
                'pointpillars/ops/voxelization/voxelization_cpu.cpp',
                'pointpillars/ops/voxelization/voxelization_cuda.cu',
            ],
            define_macros=[('WITH_CUDA', None)],
            include_dirs=['pointpillars/ops/voxelization'],
        ),
        CUDAExtension(
            name='pointpillars.ops.iou3d_op',
            sources=[
                'pointpillars/ops/iou3d/iou3d.cpp',
                'pointpillars/ops/iou3d/iou3d_kernel.cu',
            ],
            define_macros=[('WITH_CUDA', None)],
            include_dirs=['pointpillars/ops/iou3d'],
        ),
    ],
    cmdclass={'build_ext': BuildExtension},
    package_data={'pointpillars.ops': ['*.so']},
    zip_safe=False,
)