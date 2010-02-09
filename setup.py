from distutils.core import setup
import os
from admin_tools import VERSION


# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('admin_tools'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "admin_tools/" or "admin_tools\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

bitbucket_url = 'http://www.bitbucket.org/izi/django-admin-tools/'

setup(
    name='django-admin-tools',
    version=VERSION.replace(' ', '-'),
    description=('django-admin-tools is a collection of tools for the django '
                 'administration interface, it includes a full featured and '
                 'customizable dashboard, a customizable menu bar and tools '
                 'to make admin ui theming easier.'),
    author='David Jean Louis',
    author_email='izimobil@gmail.com',
    url=bitbucket_url,
    download_url='%sdownloads/django-admin-tools-%s.tar.gz' % (bitbucket_url, VERSION),
    package_dir={'admin_tools': 'admin_tools'},
    packages=packages,
    package_data={'admin_tools': data_files},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)