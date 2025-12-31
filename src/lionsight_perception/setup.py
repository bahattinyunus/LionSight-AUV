from setuptools import find_packages, setup

package_name = 'lionsight_perception'

setup(
    name=package_name,
    version='1.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bahattin Yunus Çetin',
    maintainer_email='bahattinyunus@example.com',
    description='Lionfish detection and stereo vision for LionSight-AUV',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detection_node = lionsight_perception.detection_node:main',
            'stereo_vision_node = lionsight_perception.stereo_vision_node:main',
        ],
    },
)
