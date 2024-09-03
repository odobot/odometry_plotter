from setuptools import find_packages, setup

package_name = 'odometry_plotter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cheech',
    maintainer_email='ndibapeter4@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "odometry_visualizer = odometry_plotter.odometry_visualizer:main",
            "initial_visualizer = odometry_plotter.initial_2D_wheel_visualizer:main"
        ],
    },
)
