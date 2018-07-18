from setuptools import setup

setup(
    name='byteball_rpc_client',
    version='0.0.1',
    packages=["byteball_rpc_client",],
    url='https://github.com/emre/byteball-rpc-client',
    license='MIT',
    author='emre yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A Python JSON-RPC client for the headless wallet',
    install_requires=["requests"]
)