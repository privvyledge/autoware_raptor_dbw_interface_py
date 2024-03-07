from setuptools import find_packages, setup

package_name = 'autoware_raptor_dbw_interface_py'

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
    maintainer='humble',
    maintainer_email='humble@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'autoware_raptor_dbw_interface_node = autoware_raptor_dbw_interface_py.autoware_raptor_dbw_interface_node:main'
        ],
    },
)
