from setuptools import setup
from proxy_session import __module__
from proxy_session import __version__
try:
    from pip._internal.req import parse_requirements # for pip >= 10
except ImportError:
    from pip.req import parse_requirements # for pip <= 9.0.3

def readme():
    with open('./README.md') as readme_fp:
        README = readme_fp.read()
    return README



def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.requirement) for ir in reqs]

setup(
    name=__module__,
    version=__version__,
    description='''
        {0} is a python module creates a reliable proxy request to a HTTP server.
        Current version of this module is {1}
    '''.format(__module__, __version__),
    long_description=readme(),
    long_description_content_type='text/markdown',
    url="https://github.com/antaripchatterjee/Proxy-Session",
    author="Antarip Chatterjee",
    author_email="antarip.chatterjee22@gmail.com",
    license="Unlicense",
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Software Development"
    ],
    packages=["proxy_session"],
    install_requires=load_requirements("./requirements.txt"),
    include_package_data=True
)