from setuptools import find_packages, setup

package_name = 'lionsight_mission'

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
    description='Central mission management and behavior control for LionSight-AUV',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mission_node = lionsight_mission.mission_node:main',
        ],
    },
)
