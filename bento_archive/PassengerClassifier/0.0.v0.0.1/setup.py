import os
import pip
import logging
import pkg_resources
import setuptools

def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]

try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = []

setuptools.setup(
    name='PassengerClassifier',
    version='0.0.v0.0.1',
    description="BentoML generated model module",
    long_description="""# BentoML(bentoml.ai) generated model archive
""",
    long_description_content_type="text/markdown",
    url="https://github.com/atalaya-io/BentoML",
    packages=setuptools.find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    package_data={
        'PassengerClassifier': ['bentoml.yml', 'artifacts/*']
    },
    entry_points={
        'console_scripts': [
            'PassengerClassifier=PassengerClassifier:cli',
        ],
    }
)
