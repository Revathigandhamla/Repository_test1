from setuptools import setup, find_packages
setup(
    name = 'pipeline_test1',
    version = '1.0',
    packages = find_packages(include = ('pipeline_test1*', )) + ['prophecy_config_instances.pipeline_test1'],
    package_dir = {'prophecy_config_instances.pipeline_test1' : 'configs/resources/pipeline_test1'},
    package_data = {'prophecy_config_instances.pipeline_test1' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.11'],
    entry_points = {
'console_scripts' : [
'main = pipeline_test1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
