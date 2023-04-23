from setuptools import setup
import os
from glob import glob
package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
(os.path.join('share', package_name), glob('urdf/*.urdf')),  
(os.path.join('share', package_name), glob('launch/*.py')),      
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='levin',
    maintainer_email='levinjeejan@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
      'my_circle_movement = my_package.circle_motion.py:main'
        ],
    },
)
